from config import API_KEY, MOVIE_API_URL


def get_movie_url(movie_type: str, title: str, lang: str = 'en-US'):
  return (
    f"{MOVIE_API_URL}search/{movie_type}?api_key={API_KEY}&query={title}&language={lang}"
  ) 

def get_movie_url_by_id(movie_type: str, movie_id: int, lang: str = 'en-US'):
  return (
    f"{MOVIE_API_URL}{movie_type}/{movie_id}/videos?api_key={API_KEY}&language={lang}"
  )

def get_moive_url_for_languages(movie_type: str, movie_id: int):
  return (
    f"{MOVIE_API_URL}{movie_type}/{movie_id}/translations?api_key={API_KEY}"
  )

def get_movie_url_details(movie_type: str, movie_id: int, lang: str = 'en-US'):
  return (
    f"{MOVIE_API_URL}{movie_type}/{movie_id}?api_key={API_KEY}&language={lang}&append_to_response=watch/providers"
  )

def check_release_movie_url(movie_type: str, movie_id: int):
  return (
    f"{MOVIE_API_URL}{movie_type}/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=watch/providers"
  )


