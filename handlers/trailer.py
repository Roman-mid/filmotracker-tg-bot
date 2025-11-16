from aiogram import Router, types, F
from .utils import FindCallback
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.tmdb_client import client
from constants.lang_content import lang_content
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_movie_url_by_id

router = Router()

@router.callback_query(FindCallback.filter(F.action == "trailer"))
async def show_trailer(call: types.CallbackQuery, callback_data: FindCallback, user):
    await call.answer()

    user_id = user.user_id
    user_lang = user.user_lang

    content = lang_content.get(user_lang, lang_content['en'])
    button = content['button']
    treiler = content['trailer']
    added_movie = content['movie_info']['already_added']

    movie_id = callback_data.id
    movie_type = callback_data.content_type
    lang = callback_data.lang

    details_btn = InlineKeyboardButton(
        text=button['details'],
        callback_data=FindCallback(
            action="details", 
            id=movie_id, 
            content_type=movie_type,
            lang=lang
        ).pack(),
    )
    language_btn = InlineKeyboardButton(
        text=button['providers'],
        callback_data=FindCallback(
            action="providers", 
            id=movie_id, 
            content_type=movie_type,
            lang=lang
        ).pack(),
    )

    add_btn = InlineKeyboardButton(
        text=button['add'],
        callback_data=FindCallback(
            action="add_movie", 
            id=movie_id, 
            content_type=movie_type,
            lang=lang
        ).pack()
    )

    remove_btn = InlineKeyboardButton(
        text=button['remove_from'],
        callback_data=FindCallback(
            action='remove',
            id=movie_id,
            lang=lang
        ).pack()
    )

    try:
        isFollowedFilm = await get_user_movie(user_id, movie_id)
    except Exception as e:
        print(f"Ошибка при проверки фильма в библиотеке юзера (trailer): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")

    already_added = f'\n\n✅ <i>{added_movie}</i>' if isFollowedFilm else ''

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [details_btn, language_btn],
        [remove_btn if isFollowedFilm else add_btn]
    ])
    
    url = get_movie_url_by_id(movie_type, movie_id)
    resp = await client.get(url)
    data = resp.json()

    results = data.get("results", [])
    trailer_url = None
    for video in results:
        if video.get("type") == "Trailer" and video.get("site") == "YouTube":
            trailer_url = f"https://www.youtube.com/watch?v={video.get('key')}"
            break

    if trailer_url:
        trailer = [treiler['show_trailer'](trailer_url)]
    else:
        trailer = [treiler['not_awailable']]
    trailer.append(already_added)
    text = "\n".join(trailer)

    await call.message.answer(text, reply_markup=kb, parse_mode='HTML')





