from aiogram.filters import Command
from aiogram import Router, types
from datetime import datetime, timedelta
from models import async_session, User
from payment.stripe.create_customer import create_customer
from utils.create_main_menu import create_main_menu
from constants.start_user_message import start_user_message
from pathlib import Path
from aiogram.types import FSInputFile


router = Router()
BASE_DIR = Path(__file__).parent.parent

@router.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id

    async with async_session() as session:
        user = await session.get(User, user_id)

        if not user:
            user_name = message.from_user.username
            user_lang = message.from_user.language_code
            customer = create_customer(user_id)
            image_path = Path(__file__).parent.parent / "files" / "bot_menu.bmp"
            imaage = FSInputFile(image_path)

            user = User(
                user_id=user_id,
                user_lang=user_lang,
                user_name=user_name,
                stripe_customer_id=customer.id,
                subscription_until=datetime.now() + timedelta(days=30),
                is_active=True,
            )
            session.add(user)
            await session.commit()

            user_messages = start_user_message.get(user_lang, start_user_message['en'])
            main_kb = create_main_menu(user_lang)

            await message.answer_photo(imaage, caption=user_messages['hello'](user_name), reply_markup=main_kb, parse_mode='HTML')

        else:
            user_lang = user.user_lang
            user_messages = start_user_message.get(user_lang, start_user_message['en'])
            main_kb = create_main_menu(user_lang)

            await message.answer(user_messages['exist'], reply_markup=main_kb, parse_mode='HTML')
