from aiogram import Router, types
import stripe
from aiogram.filters import Command
from config import STRIPE_APY_KEY
from constants.lang_content import lang_content

stripe.api_key = STRIPE_APY_KEY
router = Router()

@router.message(Command("unsubscribe"))
async def unsubscribe_user(message: types.Message, user):
  user_lang = user.user_lang
  content = lang_content.get(user_lang, lang_content['en'])
  payment = content['payment']

  if not user or not user.stripe_subscription_id:
    await message.answer(payment['not_found'])
    return
  
  try:
    stripe.Subscription.modify(
      user.stripe_subscription_id,
      cancel_at_period_end=True 
    )
    await message.answer(payment['stop'])

  except stripe.error.StripeError as e:
    print("Stripe error:", e)
    await message.answer(payment['fail_stop'])

