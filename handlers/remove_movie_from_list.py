from aiogram import Router, types, F
from .utils import FindCallback
from .tools.movie.remove_user_movie import remove_user_movie
from .tools.movie.get_user_movie import get_user_movie
from constants.lang_content import lang_content
from constants.errors import error

router = Router()

@router.callback_query(FindCallback.filter(F.action == 'remove_from_list'))
async def remove_movie(call: types.CallbackQuery, callback_data: FindCallback, user):
  await call.answer() # remove 'clock'

  user_id = user.user_id
  user_lang = user.user_lang

  movie_id = callback_data.id
  
  content = lang_content.get(user_lang, lang_content['en'])
  follow_list = content['follow_list']

  kb = call.message.reply_markup
  current_text = call.message.text.split("\n")

  try:
    movie_to_remove = await get_user_movie(user_id, movie_id)
  except Exception as e:
    print(f"Ошибка при проверки филь в базе (remove_movie_from_list): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await call.message.answer( error[user_lang], parse_mode='HTML')
    return

  if not movie_to_remove :
    await call.message.answer(follow_list['already_removed'])
    return

  movie_title = movie_to_remove.title

  try:
    await remove_user_movie(movie_to_remove)
  except Exception as e:
    print(f"Ошибка при удалении фильма (remove_movie_from_list): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await call.message.answer( error[user_lang], parse_mode='HTML')
    return

  movies = [line for line in current_text if f'- {movie_title}' != line]

  header = movies[0] if movies else follow_list['title']
  films = [line for line in movies[1:] if line.strip()] 

  if films:
    header = f'<b><i>{header}</i></b>'
    new_text = '\n'.join([header, ''] + films) 
  else:
    new_text = follow_list['empty_list']

  if kb and kb.inline_keyboard:
    kb.inline_keyboard = [
      row for row in kb.inline_keyboard
      if not any(button.callback_data == call.data for button in row)
    ]
    await call.message.edit_text(text=new_text, reply_markup=kb, parse_mode='HTML')

  await call.message.answer(follow_list['remove'](movie_title), parse_mode='HTML')
