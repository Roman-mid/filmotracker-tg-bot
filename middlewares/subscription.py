from aiogram import BaseMiddleware
from datetime import datetime
from aiogram.types import Message, CallbackQuery
from constants.lang_content import lang_content
from constants.start_user_message import start_user_message
from handlers.tools.user.get_user_from_db import fetch_user_from_db
from payment.stripe.stripe import stripe_create_checkout_session
from handlers.tools.user.update_user_availability import update_user_availability

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = None
        user_lang = event.from_user.language_code

        user_content = start_user_message.get(user_lang, start_user_message['en'])
        user_not_found = user_content['user_not_found']
        

        # find user_id
        if isinstance(event, Message):
            user_id = event.from_user.id
            # skip /start
            if event.text and event.text.startswith("/start"):
                return await handler(event, data)

        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
            # skip subscribe button
            if event.data and "subscribe" in event.data:
                return await handler(event, data)

        # skip if user_id is not defined
        if not user_id:
            return await handler(event, data)

        # get user
        user = await fetch_user_from_db(user_id)
        if not user:

            if isinstance(event, CallbackQuery):
                await event.message.answer(user_not_found)
            else:
                await event.answer(user_not_found)
            return
        
        data['user'] = user

        if (
            not user.is_active or 
            user.subscription_until and 
            user.subscription_until < datetime.now()
            ):
            if user.is_active:
                await update_user_availability(user_id, False)


            kb = await stripe_create_checkout_session(event.from_user.id)

            user_lang = user.user_lang
            
            content = lang_content.get(user_lang, lang_content['en'])
            subscription_expired = content['payment']['subscription_expired']

            #  sent message only for callback
            if isinstance(event, Message) and event.text:
                await event.answer(subscription_expired, parse_mode="HTML", reply_markup=kb)
                return
            elif isinstance(event, CallbackQuery) and event.data:
                await event.message.reply(subscription_expired, parse_mode="HTML", reply_markup=kb)
                
            return

        # skip middleware for not callback actions
        return await handler(event, data)




