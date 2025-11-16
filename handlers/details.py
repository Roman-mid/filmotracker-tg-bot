from aiogram import Router, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.tmdb_client import client
from constants.available_langs import available_langs
from constants.lang_content import lang_content
from constants.errors import error
from .utils import FindCallback
from .tools.movie.get_user_movie import get_user_movie
from utils.get_movie_url import get_movie_url_details

router = Router()

@router.callback_query(FindCallback.filter(F.action == "details"))
async def get_details(call: types.CallbackQuery, callback_data: FindCallback, user):
    await call.answer()  # remove "clock"

    user_id = user.user_id
    movie_id = callback_data.id
    content_type = callback_data.content_type
    lang = callback_data.lang

    user_lang = user.user_lang
    content = lang_content.get(user_lang, lang_content['en'])
    button = content['button']
    movie_info = content['movie_info']
    added_movie = movie_info['already_added']

    trailer_btn = InlineKeyboardButton(
        text=button['trailer'],
        callback_data=FindCallback(
            action="trailer", 
            id=movie_id, 
            content_type=content_type,
            lang=lang
        ).pack(),
    )
    
    language_btn = InlineKeyboardButton(
        text=button['providers'],
        callback_data=FindCallback(
            action="providers", 
            id=movie_id, 
            content_type=content_type,
            lang=lang
        ).pack(),
    )

    add_btn = InlineKeyboardButton(
        text=button['add'],
        callback_data=FindCallback(
            action="add_movie", 
            id=movie_id, 
            content_type=content_type,
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
        print(f"Ошибка при проверки фильма в библиотеке юзера (detailes): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")

    already_added = f'\n\n✅ <i>{added_movie}</i>' if isFollowedFilm else ''
                
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [trailer_btn, language_btn],
        [remove_btn if isFollowedFilm else add_btn]
    ])
    
    lang_details = user_lang if user_lang in available_langs else lang

    try:
        url = get_movie_url_details(content_type, movie_id, lang_details)
        resp = await client.get(url)
        data = resp.json()
    except Exception as e:
        print(f"Ошибка при получении данных о фильме (detailes): {e}")
        print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
        await call.message.answer( error[user_lang], parse_mode='HTML')
        return


    genres = ", ".join([g.get("name") for g in data.get("genres", [])])
    title = data.get("title") or data.get("name")
    overview = data.get("overview", "No description available")
    release_date = data.get("release_date") or data.get("first_air_date")
    rating = data.get("vote_average", "N/A")
    poster_path = data.get("poster_path")

    number_of_seasons = data.get("number_of_seasons")
    all_apisodes_number = data.get("number_of_episodes")

    last_episode_date = data.get("last_air_date")
    last_episode = data.get("last_episode_to_air", {})
    last_episode_number = last_episode.get('episode_number')
    
    next_episode = data.get("next_episode_to_air")
    
    seasons = data.get('seasons', [])
    last_season = seasons[-1] if seasons else {}
    number_of_eps = last_season.get('episode_count')

    
    number_of_episodes = (
        sum(item['episode_count'] for item in seasons[:-1]) 
        if seasons 
        else 0
    )
    
    lines = [
        f"🎬 <b>{title}</b>",
        f"{movie_info['genre']} {genres}\n",
        f"<b>{movie_info['release']} {release_date or '-'}</b>",
        f"<b>{movie_info['rating']} {rating}</b>",
    ]

    if next_episode:
        number_seasons_list = list(range(1, number_of_seasons + 1))
        number_seasons_text = ', '.join(map(str, number_seasons_list))

        lines.append(f'\n{movie_info['seasons']} {number_seasons_text}')
        if number_of_episodes:
            lines.append(f"{movie_info['number_of_episodes']} <b>{number_of_episodes + last_episode_number} / {all_apisodes_number}</b>\n")

        lines.append(f'{movie_info['current_season']}: {number_of_seasons}')
        if last_episode:
            lines.append(f"{movie_info['episodes']} <b>{last_episode_number} / {number_of_eps}</b>")
            lines.append(f"{movie_info['last_episode']} <b>{last_episode_date}</b>")
        lines.append(f"{movie_info['next_episod_date']} <b>{next_episode.get('air_date', 'N/A')}</b>")
    else :
        if content_type == 'tv':
            number_of_episodes = data.get('number_of_episodes')
            lines.append(f"\n{movie_info['seasons']} <b>{number_of_seasons}</b>")
            lines.append(f"{movie_info['number_of_episodes']} <b>{number_of_episodes}</b>")
            lines.append(f"{movie_info['last_episode']} <b>{last_episode_date}</b>")

    lines.append(f"\n{overview}")
    lines.append(already_added)

    caption = "\n".join(lines)

    if len(caption) > 1024:
        caption = caption[:1021] + "..."

    if poster_path:
        poster_url = f"https://image.tmdb.org/t/p/w342{poster_path}"
        await call.message.answer_photo(poster_url, caption=caption, parse_mode="HTML", reply_markup=kb)
    else:
        await call.message.answer(caption, parse_mode="HTML", reply_markup=kb)
