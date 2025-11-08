from models import UserMovie, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession
            
@with_db_session
async def remove_user_movie(
    movie: UserMovie,
    *, 
    session: AsyncSession
):
    async with session.begin(): 
        await session.delete(movie)
            



