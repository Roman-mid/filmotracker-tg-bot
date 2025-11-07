from models import async_session, UserMovie, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession


# async def remove_user_movie(movie: UserMovie):
#     async with async_session() as session:
#         async with session.begin(): 
#             await session.delete(movie)
            
@with_db_session
async def remove_user_movie(
    movie: UserMovie,
    *, 
    session: AsyncSession
):
    async with session.begin(): 
        await session.delete(movie)
            



