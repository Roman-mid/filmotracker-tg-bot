from sqlalchemy import update
from models import UserMovie, with_db_session
from utils.parse_date import parse_date
from sqlalchemy.ext.asyncio import AsyncSession

@with_db_session
async def update_movie_release(
  user_id: int, 
  movie_id: int, 
  next_date: str | None,
  *,
  session: AsyncSession
):
  stmt = (update(UserMovie)
          .where(UserMovie.user_id == user_id, UserMovie.movie_id == movie_id)
          .values(next_release_date=parse_date(next_date) if next_date else None)
  )
  await session.execute(stmt)
  await session.commit()
