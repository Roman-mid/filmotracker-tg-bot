from sqlalchemy import select
from models import async_session, User

async def get_all_active_users() -> list[User] | None:
  async with async_session() as session:
    result = await session.execute(select(User).where(User.is_active == True))
    return result.scalars().all()
  

  
async def get_all_users() -> list[User] | None:
  async with async_session() as session:
    users = await session.execute(select(User))
    return users.scalars().all()