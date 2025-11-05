from aiogram import Router, types, F
from pathlib import Path
from aiogram.types import FSInputFile
import asyncio
from constants.lang_content import lang_content

router = Router()
BASE_DIR = Path(__file__).parent.parent

user_media  = []

@router.message(~F.text, ~F.successful_payment) 
async def not_text_message(message: types.Message, user):
  user_media.append(message)

  # user_lang = message.from_user.language_code
  user_lang = user.user_lang
  content = lang_content.get(user_lang, lang_content['en'])
  stop_message = content['stop']

  stop = Path(__file__).parent.parent / "files" / "stop.gif"
  animation_stop = FSInputFile(stop) 

  cry = Path(__file__).parent.parent / "files" / "cry.gif"
  animation_cry = FSInputFile(cry) 

  if len(user_media) == 1:
    asyncio.create_task(clear_user_media())  # run async task to remove media
    await message.answer(stop_message['first'])

  if len(user_media) == 2:
    await message.answer(stop_message['second'])

  if len(user_media) == 3:
    await message.answer_animation(animation=animation_stop, caption=stop_message['third'])

  if len(user_media) > 3:
    await message.answer_animation(animation=animation_cry, caption=stop_message['last'])



async def clear_user_media():
  global user_media
  await asyncio.sleep(15 * 60)  # wait 15 minutes
  if user_media:
    user_media = []
