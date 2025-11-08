from aiogram import Router, types, F
from .utils import FindCallback
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

    try:
        kb = await stripe_create_checkout_session(user_id)
        await callback.message.edit_text(payment_title, reply_markup=kb)
        await callback.answer()
    except Exception as e:
        print(f"Ошибка при создании stripe сессии (send_subscription_invoice): {e}")
        print(f"[ERROR], user_id={user_id}, {type(e).__name__}: {e}")
        await callback.message.answer(user_id, error[user_lang], parse_mode='HTML')
