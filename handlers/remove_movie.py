from aiogram import Router, types, F
from .utils import FindCallback
from .tools.movie.remove_user_movie import remove_user_movie
from .tools.movie.get_user_movie import get_user_movie
from constants.lang_content import lang_content
from constants.errors import error

router = Router()

@router.callback_query(FindCallback.filter(F.action == 'remove'))
async def remove_movie(call: types.CallbackQuery, callback_data: FindCallback, user):
  await call.answer() # remove 'clock'

  user_id = user.user_id
  user_lang = user.user_lang

  movie_id = callback_data.id

  content = lang_content.get(user_lang, lang_content['en'])
  follow_list = content['follow_list']

  
  try:
    movie_to_remove = await get_user_movie(user_id, movie_id)
  except Exception as e:
    print(f"Ошибка при проверки филь в базе (remove_movie): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await call.message.answer( error[user_lang], parse_mode='HTML')
    return


  # movie_to_remove = await get_user_movie(user_id, movie_id)

  if not movie_to_remove :
    await call.message.answer(follow_list['already_removed'])
    return

  movie_title = movie_to_remove.title

  # await remove_user_movie(movie_to_remove)

  try:
    await remove_user_movie(movie_to_remove)
  except Exception as e:
    print(f"Ошибка при удалении фильма (remove_movie): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await call.message.answer( error[user_lang], parse_mode='HTML')
    return

  await call.message.answer(follow_list['remove'](movie_title), parse_mode='HTML')


