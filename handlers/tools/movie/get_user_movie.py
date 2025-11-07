from sqlalchemy import and_, select
from models import async_session, UserMovie, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession


# async def get_user_movie(user_id: str, movie_id: str) -> UserMovie:
#   async with async_session() as session:
#     async with session.begin(): 
#       result = await session.execute(
#         select(UserMovie).where(
#           and_(
#             UserMovie.user_id == user_id ,
#             UserMovie.movie_id == movie_id
#           )
#         )
#       )
#       return result.scalar_one_or_none()


# async def get_all_user_movie(user_id: str) -> list[UserMovie]:
#   async with async_session() as session:
#     result = await session.execute(select(UserMovie).where(UserMovie.user_id == user_id))
#     return result.scalars().all()

@with_db_session
async def get_user_movie(
  user_id: str, 
  movie_id: str,
  *, 
  session: AsyncSession
) -> UserMovie:
  async with session.begin(): 
    result = await session.execute(
      select(UserMovie).where(
        and_(
          UserMovie.user_id == user_id ,
          UserMovie.movie_id == movie_id
        )
      )
    )
    return result.scalar_one_or_none()

@with_db_session
async def get_all_user_movie(
  user_id: str, 
  *, 
  session: AsyncSession
) -> list[UserMovie]:
  result = await session.execute(select(UserMovie).where(UserMovie.user_id == user_id))
  return result.scalars().all()
  