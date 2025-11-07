from sqlalchemy import update
from models import async_session, User, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession



# async def update_user_lang(user_id: int, lang: str):
#   async with async_session() as session:
#     stmt = (
#       update(User)
#       .where(User.user_id == user_id)
#       .values(user_lang=lang)
#     )

#     await session.execute(stmt)
#     await session.commit()

@with_db_session
async def update_user_lang(user_id: int, lang: str, *, session: AsyncSession):
  stmt = (
    update(User)
    .where(User.user_id == user_id)
    .values(user_lang=lang)
  )

  await session.execute(stmt)
  await session.commit()