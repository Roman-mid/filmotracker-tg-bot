from services.tmdb_client import client
from config import GOOGLE_APPLICATION_CREDENTIALS
from constants.lang_content import lang_content
from constants.errors import error
from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .utils import FindCallback
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_movie_url

router = Router()

# creds = service_account.Credentials.from_service_account_file(
#     GOOGLE_APPLICATION_CREDENTIALS
# )
creds = service_account.Credentials.from_service_account_info(
    GOOGLE_APPLICATION_CREDENTIALS
)
translate_client = translate.Client(credentials=creds)

@router.message(F.text & ~F.text.startswith("/"))
async def choose_type(message: types.Message, user):

    user_lang = user.user_lang
    content = lang_content.get(user_lang, lang_content['en'])
    find_movie = content['button']['find_movie']
    find_serial = content['button']['find_tv']

    buttons = [
        [
            InlineKeyboardButton(text=f' {find_movie} ', callback_data="movies"),
            InlineKeyboardButton(text=f' {find_serial} ', callback_data="serials"),
        ],
       
    ]
    await message.answer(message.text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))


@router.callback_query(F.data.in_({"movies", "serials"}))
async def get_request(call: types.CallbackQuery, user):

    user_id = user.user_id
    user_lang = user.user_lang
    content_dic = lang_content.get(user_lang, lang_content['en'])
    button = content_dic['button']
    message = content_dic['message']
    added_movie = content_dic['movie_info']['already_added']

    movie_type = "movie" if call.data == "movies" else "tv"
    title = call.message.text.lower().strip()

    result_trans = translate_client.detect_language(title)
    lang = result_trans.get('language') or 'en'

    try:
        url = get_movie_url(movie_type, title, lang)
        resp = await client.get(url)
        result = resp.json().get("results", [])
    except Exception as e:
        print(f"Ошибка при поиске фильма в API фильма (search): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        await call.message.answer(user_id, error[user_lang], parse_mode='HTML')
        return

    if not result:
        await call.message.reply(message['not_found'])
        return

    reversed_result = [
        el for el in result
        if title in (el.get("title") or "").lower()
        or title in (el.get("name") or "").lower()
    ][::-1]

    for content in reversed_result:
        movie_title = content.get('title') or content.get('name')
        release_date = content.get('release_date') or content.get("first_air_date")
        desc = content.get('overview', message['no_descriptions'])

        poster = content.get("poster_path")
        content_id = content.get("id")
    
        try:
            isFollowedFilm = await get_user_movie(user_id, content_id)
        except Exception as e:
            print(f"Ошибка при проверки фильма в библиотеке юзера (detailes): {e}")
            print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        
        already_added = f'\n\n✅ <i>{added_movie}</i>' if isFollowedFilm else ''

        caption = (
            f"🎬 <b>{movie_title}</b>\n{release_date or ''}\n\n{desc[:200]}...{already_added}"
        )

        add_btn = InlineKeyboardButton(
            text=button['add'],
            callback_data=FindCallback(
                action="add_movie", 
                id=content_id, 
                content_type=movie_type,
                lang=lang
            ).pack()
        )

        keyboard=[
                [
                    InlineKeyboardButton(
                        text=button['details'],
                        callback_data=FindCallback(
                            action="details", 
                            id=content_id, 
                            content_type=movie_type,
                            lang=lang
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text=button['trailer'],
                        callback_data=FindCallback(
                            action="trailer", 
                            id=content_id, 
                            content_type=movie_type,
                            lang=lang
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text=button['languages'],
                        callback_data=FindCallback(
                            action="languages", 
                            id=content_id, 
                            content_type=movie_type,
                            lang=lang
                        ).pack()
                    ),
                ],
            ]

        if not isFollowedFilm:
            keyboard.append([add_btn])

        kb = InlineKeyboardMarkup(inline_keyboard=keyboard)

        if poster:
            await call.message.answer_photo(f"https://image.tmdb.org/t/p/w500{poster}", caption=caption, reply_markup=kb, parse_mode='HTML')
        else:
            await call.message.answer(caption, reply_markup=kb, parse_mode='HTML')

