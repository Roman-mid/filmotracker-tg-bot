from services.tmdb_client import client
from constants.lang_content import lang_content
from constants.errors import error
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import FindCallback
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_movie_url_details

router = Router()

@router.callback_query(FindCallback.filter(F.action == "providers"))
async def show_languages(call: types.CallbackQuery, callback_data: FindCallback, user):
    await call.answer()

    user_id = user.user_id
    user_lang = user.user_lang
    content = lang_content.get(user_lang, lang_content['en'])

    message = content['message']
    button = content['button']
    # languages = content['languages']
    providers = content['providers']
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

    try:
        url = get_movie_url_details(movie_type, movie_id)
        resp = await client.get(url)
        data = resp.json()  
    except Exception as e:
        print(f"Ошибка при получении данных о фильме (detailes): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        await call.message.answer( error[user_lang], parse_mode='HTML')
        return

    providers_result = data.get('watch/providers')['results']
    if providers:
        provider_names_list = list({provider['provider_name'] 
                            for country in providers_result.values() 
                            for provider in country.get('flatrate', [])})
    else:
        provider_names_list = [message['no_information_available']]

    title = data.get("title") or data.get("name")

    provider_names_list.append(already_added)
    text = "\n".join(provider_names_list)

    await call.message.answer(providers(title, text), reply_markup=kb, parse_mode='HTML')
