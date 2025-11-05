from models import async_session, UserMovie

async def remove_user_movie(movie: UserMovie):
    async with async_session() as session:
        async with session.begin(): 
            await session.delete(movie)
            
            



