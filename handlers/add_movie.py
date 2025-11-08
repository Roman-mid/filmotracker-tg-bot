from aiogram import Router, types, F
from .utils import FindCallback
from services.tmdb_client import client
from constants.lang_content import lang_content
from constants.errors import error
from datetime import datetime, date
from .tools.movie.add_user_movie import add_user_movie
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_movie_url_details
from utils.parse_date import parse_date

router = Router()

@router.callback_query(FindCallback.filter(F.action == 'add_movie'))
async def add_movie(call: types.CallbackQuery, callback_data: FindCallback, user):
    await call.answer()  # remove "clock"

    user_id = user.user_id
    user_lang = user.user_lang

    movie_id = callback_data.id
    movie_type = callback_data.content_type
    lang = callback_data.lang

    content = lang_content.get(user_lang, lang_content['en'])
    add_movie = content['add_movie']

    try:
        url = get_movie_url_details(movie_type, movie_id, lang)
        resp = await client.get(url)
        resp.raise_for_status()  # check HTTP error (aiohttp/httpx)
        data = resp.json()
    except Exception as e:
        print(f"Ошибка при получении данных о фильме: {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        await call.message.answer( error[user_lang], parse_mode='HTML')
        return
    
    title = data.get("title") or data.get("name")   
    next_release_date = None

    if movie_type == 'tv':
        next_episode = data.get('next_episode_to_air', {}) 
        next_release_date = next_episode.get('air_date') if next_episode else None
    else:
        release_movie_date = data.get('release_date')
        next_release_date = release_movie_date if parse_date(release_movie_date) >= date.today() else None

    next_release_DATE = (
        datetime.strptime(next_release_date, "%Y-%m-%d").date()
        if next_release_date else None
    )

    try:
        movie_in_db = await get_user_movie(user_id, movie_id)
    except Exception as e:
        print(f"Ошибка при проверке фильма в базе: {e}")
        await call.message.answer( error[user_lang])
        return

    if movie_in_db:
        await call.message.answer(add_movie['already_added'](title), parse_mode="HTML")
        return

    try:
        await add_user_movie(
            user_id,
            movie_id,
            title,
            lang,
            movie_type,
            next_release_DATE
        )
        await call.message.answer(add_movie['add'](title), parse_mode="HTML")
    except Exception as e:
        print(f"Ошибка при добавлении фильма в базу: {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        await call.message.answer( error[user_lang])



