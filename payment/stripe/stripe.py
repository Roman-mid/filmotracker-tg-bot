import stripe
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_KEY, MASTER_ID, PAYMENT_KEY, STRIPE_PROD_ID,STRIPE_APY_KEY, STRIPE_PRICE_ID
from handlers.tools.user.get_user_from_db import fetch_user_from_db
from constants.lang_content import lang_content

router = Router()
stripe.api_key = STRIPE_APY_KEY 

async def stripe_create_checkout_session(user_id: int):

  try:
    user = await fetch_user_from_db(user_id)
  except Exception as e:
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    return


  user_lang = user.user_lang
  content = lang_content.get(user_lang, lang_content['en'])
  subscribe = content['button']['subscribe']

  try:

    session = stripe.checkout.Session.create(
      payment_method_types=["card"],
      mode="subscription",
      customer=user.stripe_customer_id,
      line_items=[{
        "price": STRIPE_PRICE_ID,
        "quantity": 1,
      }],
      success_url="https://unfuelled-uninjuring-scarlette.ngrok-free.dev/success?session_id={CHECKOUT_SESSION_ID}",
      cancel_url="https://unfuelled-uninjuring-scarlette.ngrok-free.dev/cancel",
      # success_url="https://unfuelled-uninjuring-scarlette.ngrok-free.dev/static/success.html",
      # cancel_url="https://unfuelled-uninjuring-scarlette.ngrok-free.dev/static/cancel.html",
      client_reference_id=str(user_id),  # connect with Telegram user_id
      metadata={"tg_user_id": str(user_id)}, 
    )
  except stripe.error.StripeError as e:
    print(f"[Stripe ERROR], user_id={user_id}: {e}")
    return

  kb = InlineKeyboardMarkup(
    inline_keyboard=[
      [InlineKeyboardButton(text=f"🔔   {subscribe}   🔔", url=session.url)]
    ]
  )
  return kb