from services.tmdb_client import client
from config import API_KEY, MASTER_ID, PAYMENT_KEY
from constants.lang_content import lang_content
from .tools.movie.get_new_released_movies import get_new_released_movies
from .tools.movie.update_movie_release import update_movie_release
from .tools.user.update_user_availability import update_user_availability
from payment.stripe.stripe import stripe_create_checkout_session
from utils.get_movie_url import check_release_movie_url
from utils.parse_date import parse_date
from datetime import datetime, date

async def check_follow_list(bot, user):
  user_id = user.user_id
  user_lang = user.user_lang
  content = lang_content.get(user_lang, lang_content['en'])
  subscription_expired = content['payment']['subscription_expired']
  release = content['release']
  new_ep_info = content['next_episode_info']

  if user and (user.subscription_until < datetime.now() or not user.is_active):
  # if (user and (user.subscription_until < datetime.now() or not user.is_active)) and user_id != MASTER_ID:

    if user.is_active:
      try:
        await update_user_availability(user_id, False)
      except Exception as e:
        print(f"Ошибка при деактивации юзера (check_follow_list): {e}")
        print(f"[ERROR], user_id={user_id}, {type(e).__name__}: {e}")
        return

    kb = await stripe_create_checkout_session(user_id)
    
    try:
      await bot.send_message( 
        user_id, 
        subscription_expired, 
        parse_mode="HTML", 
        reply_markup=kb
      )
    except Exception as e:
      print(f"Ошибка при создании stripe сессии (check_follow_list): {e}")
      print(f"[ERROR], user_id={user_id}, {type(e).__name__}: {e}")
    
    return
  
  user_movies = await get_new_released_movies(user_id)
  if not user_movies:
    return  

  for movie in user_movies:
    movie_type = movie.movie_type
    movie_id = movie.movie_id
    movie_title = movie.title

    url = check_release_movie_url(movie_type, movie_id)
    try:
      resp = await client.get(url)
      data = resp.json()
    except Exception as e:
      print(f"[TMDB error] {e}")
      continue

    if not data:
      continue

    poster = data.get('poster_path')
    next_episode_to_air = None

    if movie_type == 'tv':
      next_episode = data.get("next_episode_to_air") or {}
      next_episode_to_air = next_episode.get("air_date") 

      if movie.next_release_date == date.today():
        last_season = data.get('seasons', [])[-1] if data.get('seasons') else None
        number_of_eps = last_season.get('episode_count')

        next_ep_name = next_episode.get('name')
        next_ep_desc = next_episode.get('overview')
        next_ep_number = next_episode.get('episode_number')
        next_ep_sesons_number = next_episode.get('season_number')

        message = [
          f'{release['new_episod']}\n', 
          f'{new_ep_info['title']}: {next_ep_name}',
          f'{new_ep_info['episode_number']}: {next_ep_number} / {number_of_eps}',
          f'{new_ep_info['season_number']}: {next_ep_sesons_number}\n',
          f'{next_ep_desc}\n',
          f"{'❗ <i><b>LAST EPISODE</b></i> ❗' if next_ep_number == number_of_eps else ''}"
        ]

        message_text = '\n'.join(message)

        if poster:
          image_url = f"https://image.tmdb.org/t/p/w342{poster}"
          await bot.send_photo(chat_id=user_id, photo=image_url, 
          caption=message_text, parse_mode="HTML")

        else :
          await bot.send_message(user_id, message_text, parse_mode="HTML")

    else :
      overview = data.get('overview')
      message_text =f"{release['movie'](movie_title)}\n\n {overview}"

      if poster:
        image_url = f"https://image.tmdb.org/t/p/w342{poster}"
        await bot.send_photo(chat_id=user_id, photo=image_url, 
        caption=message_text, parse_mode="HTML")

      else :
        await bot.send_message(user_id, message_text, parse_mode="HTML")

    
    await update_movie_release(movie.user_id, movie.movie_id, next_episode_to_air)
   
