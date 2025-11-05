from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import FindCallback
from aiogram.filters import Command
from pathlib import Path
from .tools.movie.get_user_movie import get_all_user_movie
from constants.lang_content import lang_content
from constants.commands import movie_list_tuple
from constants.errors import error

router = Router()
BASE_DIR = Path(__file__).parent.parent

@router.message(lambda msg: msg.text in movie_list_tuple)
async def show_follow_list(message: types.Message, user):
  user_id = user.user_id
  user_lang = user.user_lang
  content = lang_content.get(user_lang, lang_content['en'])
  button = content['button']
  follow = content['follow_list']


  try:
    follow_list = await get_all_user_movie(user_id)
  except Exception as e:
    print(f"Ошибка при получении юиюлиотеки юзера (show_follow_list): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await message.answer(user_id, error[user_lang], parse_mode='HTML')
    return
  
  if not follow_list:
    await message.answer(follow['empty_list'], parse_mode='HTML')
    return
  
  text_lins = [follow['title']]
  keyboard_rows = []

  for item in follow_list:

    movie_title = item.title
    movie_id = item.movie_id
    movie_type = item.movie_type
    lang = item.lang

    text_lins.append(f'- {movie_title}')
    
    keyboard_rows.append([
      InlineKeyboardButton(
        text=f'   {movie_title} | {button['details']}   ', 
        callback_data=FindCallback(
          action='details',
          id=movie_id,
          content_type=movie_type,
          lang=lang
        ).pack()
      ),
      InlineKeyboardButton(
        text=button['remove'],
        callback_data=FindCallback(
          action='remove_from_list',
          id=movie_id,
        ).pack()
      )
    ])
  
  text ='\n'.join(text_lins)
  kb = InlineKeyboardMarkup(inline_keyboard=keyboard_rows)

  await message.answer(text, reply_markup=kb, parse_mode='HTML')



