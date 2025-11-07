from datetime import date
from models import async_session, UserMovie, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession


# async def add_user_movie(
#     user_id: str,
#     movie_id: str,
#     title: str,
#     lang: str,
#     movie_type: str,  # 'movie' | 'tv'
#     next_release_date: date
# ):
#   async with async_session() as session:
#     movie = UserMovie(
#         user_id=user_id,
#         movie_id=movie_id,
#         title=title,
#         lang=lang,
#         movie_type=movie_type,
#         next_release_date=next_release_date
#     )
#     session.add(movie)
#     await session.commit()

@with_db_session
async def add_user_movie(
  user_id: str,
  movie_id: str,
  title: str,
  lang: str,
  movie_type: str,  # 'movie' | 'tv'
  next_release_date: date,
  *,
  session: AsyncSession
):
  movie = UserMovie(
    user_id=user_id,
    movie_id=movie_id,
    title=title,
    lang=lang,
    movie_type=movie_type,
    next_release_date=next_release_date
  )
  session.add(movie)
  await session.commit()
