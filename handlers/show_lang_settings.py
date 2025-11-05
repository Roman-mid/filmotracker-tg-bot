from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import FindCallback
from constants.commands import langs_tuple, user_languages

router = Router()

@router.message(lambda msg: msg.text in langs_tuple)
async def show_lang_settings(message: types.Message, user):

  user_lang = user.user_lang
  msg_title = user_languages.get(user_lang, user_languages['en'])['title']

  keyboard_rows = []

  for key in user_languages:
    keyboard_rows.append([
      InlineKeyboardButton(
        text=user_languages[key]['label'], 
        callback_data=FindCallback(
          action='update_user_lang',
          lang=key
        ).pack()
      ),
    ])

  kb = InlineKeyboardMarkup(inline_keyboard=keyboard_rows)

  await message.answer(text=msg_title, reply_markup=kb)
