from models import async_session, User, with_db_session
from models import User
from sqlalchemy.ext.asyncio import AsyncSession


# async def fetch_user_from_db(user_id: int) -> User | None:
#     async with async_session() as session:
#         user = await session.get(User, user_id)
#         return user
    

@with_db_session
async def fetch_user_from_db(
    user_id: int, 
    *, 
    session: AsyncSession
) -> User | None:
    user = await session.get(User, user_id)
    return user


