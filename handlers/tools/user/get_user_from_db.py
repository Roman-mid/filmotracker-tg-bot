from models import async_session, User
from models import User

async def fetch_user_from_db(user_id: int) -> User | None:
    async with async_session() as session:
        user = await session.get(User, user_id)
        return user


