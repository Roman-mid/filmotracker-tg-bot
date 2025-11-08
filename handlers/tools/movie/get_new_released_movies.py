from sqlalchemy import select, and_
from models import UserMovie, with_db_session
from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession 

@with_db_session
async def get_new_released_movies(
  user_id, 
  *, 
  session: AsyncSession
) -> list[UserMovie] | None:
  result = await session.execute(select(UserMovie).where(
    and_(
      UserMovie.user_id == user_id, 
      UserMovie.next_release_date <= date.today())
    )
  )

  return result.scalars().all()