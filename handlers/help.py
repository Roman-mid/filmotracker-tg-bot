
from aiogram import Router, types
from constants.commands import help_tuple
from constants.start_user_message import start_user_message
from pathlib import Path
from aiogram.types import FSInputFile

router = Router()

@router.message(lambda msg: msg.text in help_tuple)
async def help(message: types.Message, user):

  image_path = Path(__file__).parent.parent / "files" / "bot_menu.bmp"
  imaage = FSInputFile(image_path)

  user_name = user.user_name
  user_lang = user.user_lang

  help_message = start_user_message.get(user_lang, start_user_message['en'])['hello'](user_name)

  await message.answer_photo(imaage, caption=help_message,  parse_mode='HTML')
