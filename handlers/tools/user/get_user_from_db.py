from models import User, with_db_session
from models import User
from sqlalchemy.ext.asyncio import AsyncSession

@with_db_session
async def fetch_user_from_db(
    user_id: int, 
    *, 
    session: AsyncSession
) -> User | None:
    user = await session.get(User, user_id)
    return user


