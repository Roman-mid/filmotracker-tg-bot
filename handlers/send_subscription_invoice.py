from config import PAYMENT_KEY
from aiogram import Router, types, F
from .utils import FindCallback
from aiogram.types import LabeledPrice
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from payment.stripe.stripe import stripe_create_checkout_session
from constants.lang_content import lang_content
from constants.errors import error

router = Router()
@router.callback_query(FindCallback.filter(F.action == "subscribe_"))
async def subscribe_callback(callback: types.CallbackQuery, user):
    user_lang = user.user_lang
    user_id = callback.from_user.id
    content = lang_content.get(user_lang, lang_content['en'])
    payment_title = content['payment']['title']

    # kb = await stripe_create_checkout_session(callback.from_user.id)
    # await callback.message.edit_text(payment_title, reply_markup=kb)
    # await callback.answer()

    try:
        kb = await stripe_create_checkout_session(user_id)
        await callback.message.edit_text(payment_title, reply_markup=kb)
        await callback.answer()
    except Exception as e:
        print(f"Ошибка при создании stripe сессии (send_subscription_invoice): {e}")
        print(f"[ERROR], user_id={user_id}, {type(e).__name__}: {e}")
        await callback.message.answer(user_id, error[user_lang], parse_mode='HTML')






# -------------------
# @router.callback_query(FindCallback.filter(F.action == "subscribe"))
# async def send_subscription_invoice(call: types.CallbackQuery, callback_data: FindCallback):
#     await call.answer() 

#     user_id = call.from_user.id
#     payload = f"subscription:{user_id}"
#     prices = [LabeledPrice(label="Monthly subscription", amount=200)] # 2 USD 

#     # Smart Glocal
#     await call.message.answer_invoice(
#         title="Subscription",
#         description="Monthly subscription for premium features",
#         payload=payload, 
#         provider_token=PAYMENT_KEY,
#         currency="USD", 
#         prices=prices,
#         start_parameter="subscribe",
#         save_card=True
#         show_recurrent_checkbo=True
#     )

# @router.callback_query(FindCallback.filter(F.action == "subscribe"))
# async def choose_payment_system(call: types.CallbackQuery):
#     kb = InlineKeyboardMarkup(inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="💳 Stripe (card)", 
#                 callback_data=FindCallback(
#                     action="pay_stripe"
#                 ).pack()
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="🅿️ PayPal", 
#                 callback_data=FindCallback(
#                     action="ay_paypal"
#                 ).pack()
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="🪙 Crypto (USDT/BTC)", 
#                 callback_data=FindCallback(
#                     action="pay_crypto"
#                 ).pack()
#             )
#         ],
#         [
#             InlineKeyboardButton(
#                 text="🤖 Smart Glocal (Telegram Pay)", 
#                 callback_data=FindCallback(
#                     action="pay_glocal"
#                 ).pack()
#             )
#         ],
#     ])
#     await call.message.answer("Select the payment sistem:", reply_markup=kb)