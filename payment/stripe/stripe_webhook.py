from aiohttp import web
import stripe
from aiogram import Bot
from constants.lang_content import lang_content
from constants.errors import error
from config import BOT_KEY, STRIPE_WEBHOOK, STRIPE_APY_KEY
from .save_stripe_customer_id import save_stripe_customer_id
from .get_user_by_stripe_customer_id import get_user_by_stripe_customer_id
from .save_stripe_subscription_id import save_stripe_subscription_id
from handlers.tools.user.get_user_from_db import fetch_user_from_db
from payment.stripe.stripe import stripe_create_checkout_session
from handlers.tools.user.update_user_availability import update_user_availability

bot = Bot(token=BOT_KEY)
stripe.api_key = STRIPE_APY_KEY 


# Universal handle error
async def handle_error(user_id: int, e: Exception, user_lang: str = "en"):
    print(f"[ERROR] user_id={user_id} | {type(e).__name__}: {e}")
    try:
        await bot.send_message(
            int(user_id),
            error.get(user_lang, error["en"]),
            parse_mode="HTML"
        )
    except Exception as send_err:
        print(f"⚠️ Ошибка при отправке сообщения пользователю {user_id}: {send_err}")


# MAIN webhook
async def stripe_webhook(request: web.Request):
    print("📩 Webhook received!")
    payload = await request.text()
    sig_header = request.headers.get("Stripe-Signature")

    # check Stripe
    try:
        event = stripe.Webhook.construct_event(
            payload, 
            sig_header, 
            STRIPE_WEBHOOK
        )
    except ValueError:
        print("❌ Invalid payload")
        return web.Response(status=400)
    except stripe.error.SignatureVerificationError:
        print("❌ Invalid signature")
        return web.Response(status=400)

    # === checkout.session.completed ===
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        user_id = session.get("client_reference_id") or session.get("metadata", {}).get("tg_user_id")
        customer_id = session.get("customer")

        if not user_id:
            print("⚠️ Missing user_id in checkout.session.completed")
            return web.Response(status=200)

        try:
            user = await fetch_user_from_db(int(user_id))
            user_lang = getattr(user, "user_lang", "en")
        except Exception as e:
            await handle_error(user_id, e)
            return web.Response(status=200)

        content = lang_content.get(user_lang, lang_content["en"])
        payment = content["payment"]

        try:
            await save_stripe_customer_id(user_id, customer_id)
            await bot.send_message(int(user_id), payment["session_completed"])
            print(f"✅ Checkout completed for user {user_id}")
        except Exception as e:
            await handle_error(user_id, e, user_lang)

    # === customer.subscription.created ===
    elif event["type"] == "customer.subscription.created":
        subscription = event["data"]["object"]
        customer_id = subscription.get("customer")
        subscription_id = subscription.get("id")

        try:
            user = await get_user_by_stripe_customer_id(customer_id)
        except Exception as e:
            print(f"Ошибка при получении пользователя по customer_id: {e}")
            return web.Response(status=200)

        if user and subscription_id:
            try:
                await save_stripe_subscription_id(customer_id, subscription_id)
                print(f"✅ Subscription created for user {user.user_id}")
            except Exception as e:
                await handle_error(user.user_id, e, user.user_lang)

    # === invoice.payment_succeeded ===
    elif event["type"] == "invoice.payment_succeeded":
        invoice = event["data"]["object"]
        customer_id = invoice.get("customer")

        try:
            user = await get_user_by_stripe_customer_id(customer_id)
        except Exception as e:
            print(f"Ошибка получения пользователя (invoice.payment_succeeded): {e}")
            return web.Response(status=200)

        if user:
            user_lang = getattr(user, "user_lang", "en")
            content = lang_content.get(user_lang, lang_content["en"])
            payment = content["payment"]

            try:
                await update_user_availability(user.user_id, True)
                if not user.is_active:
                    await bot.send_message(user.user_id, payment["payment_succeeded"])
                print(f"✅ Payment succeeded for user {user.user_id}")
            except Exception as e:
                await handle_error(user.user_id, e, user_lang)

    # === invoice.payment_failed ===
    elif event["type"] == "invoice.payment_failed":
        invoice = event["data"]["object"]
        customer_id = invoice.get("customer")

        try:
            user = await get_user_by_stripe_customer_id(customer_id)
        except Exception as e:
            print(f"Ошибка invoice.payment_failed - get_user_by_stripe_customer_id: {e}")
            return web.Response(status=200)

        if user:
            user_lang = getattr(user, "user_lang", "en")
            content = lang_content.get(user_lang, lang_content["en"])
            payment = content["payment"]
            await bot.send_message(user.user_id, payment["payment_failed"])
            print(f"⚠️ Payment failed for user {user.user_id}")

    # === customer.subscription.deleted ===
    elif event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        customer_id = subscription.get("customer")

        try:
            user = await get_user_by_stripe_customer_id(customer_id)
        except Exception as e:
            print(f"Ошибка получения пользователя (subscription.deleted): {e}")
            return web.Response(status=200)

        if user:
            user_id = user.user_id
            user_lang = getattr(user, "user_lang", "en")
            content = lang_content.get(user_lang, lang_content["en"])
            payment = content["payment"]
            kb = await stripe_create_checkout_session(user_id)

            try:
                await update_user_availability(user_id, False)
                await bot.send_message(
                    user_id,
                    payment["subscription_expired"],
                    reply_markup=kb,
                    parse_mode="HTML"
                )
                print(f"🧾 Subscription expired for user {user_id}")
            except Exception as e:
                await handle_error(user_id, e, user_lang)

    # === Handle unknown events ===
    else:
        print(f"ℹ️ Unhandled event type: {event['type']}")

    return web.Response(status=200)


# app = web.Application()
# app.router.add_post("/stripe/webhook", stripe_webhook)

