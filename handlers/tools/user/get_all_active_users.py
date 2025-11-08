from sqlalchemy import select
from models import User, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession

@with_db_session
async def get_all_active_users(*, session: AsyncSession) -> list[User] | None:
  result = await session.execute(select(User).where(User.is_active == True))
  return result.scalars().all()
  
@with_db_session
async def get_all_users(*, session: AsyncSession) -> list[User] | None:
  users = await session.execute(select(User))
  return users.scalars().all()
