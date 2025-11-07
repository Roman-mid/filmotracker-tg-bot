from sqlalchemy import select
from models import async_session, engine, User, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_active_users() -> list[User] | None:
  async with async_session() as session:
    result = await session.execute(select(User).where(User.is_active == True))
    return result.scalars().all()
  
  
# async def get_all_users() -> list[User] | None:
#   async with async_session() as session:
#     users = await session.execute(select(User))
#     return users.scalars().all()

    
@with_db_session
async def get_all_users(*, session: AsyncSession) -> list[User] | None:
  users = await session.execute(select(User))
  return users.scalars().all()
