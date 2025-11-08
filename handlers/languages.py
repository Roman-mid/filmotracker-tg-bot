from services.tmdb_client import client
from constants.lang_content import lang_content
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import FindCallback
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_moive_url_for_languages

router = Router()

@router.callback_query(FindCallback.filter(F.action == "languages"))
async def show_languages(call: types.CallbackQuery, callback_data: FindCallback, user):
    await call.answer()

    user_id = user.user_id
    user_lang = user.user_lang
    content = lang_content.get(user_lang, lang_content['en'])

    message = content['message']
    button = content['button']
    languages = content['languages']
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
    trailer_btn = InlineKeyboardButton(
        text=button['trailer'],
        callback_data=FindCallback(
            action="trailer", 
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
        print(f"Ошибка при проверки фильма в библиотеке юзера (languages): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    
    already_added = f'\n\n✅ <i>{added_movie}</i>' if isFollowedFilm else ''

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [details_btn, trailer_btn],
        [remove_btn if isFollowedFilm else add_btn]
    ])

    url = get_moive_url_for_languages(movie_type, movie_id)
    resp = await client.get(url)
    data = resp.json()

    translations = data.get("translations", [])
    if translations:
        langs = [t.get("name") or t.get("english_name") or "N/A" for t in translations]
    else:
        langs = [message['no_information_available']]
    
    langs.append(already_added)

    langs_text = "\n ".join(langs)

    await call.message.answer(languages(langs_text), reply_markup=kb, parse_mode='HTML')
