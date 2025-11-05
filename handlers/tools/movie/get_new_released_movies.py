from sqlalchemy import select, and_
from models import async_session, UserMovie
from datetime import date

async def get_new_released_movies(user_id) -> list[UserMovie] | None:
  async with async_session() as session:
    result = await session.execute(select(UserMovie).where(
      and_(
        UserMovie.user_id == user_id, 
        UserMovie.next_release_date <= date.today())
      )
    )

    return result.scalars().all()
  