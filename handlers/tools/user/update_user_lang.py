from sqlalchemy import update
from models import User, with_db_session
from sqlalchemy.ext.asyncio import AsyncSession


@with_db_session
async def update_user_lang(user_id: int, lang: str, *, session: AsyncSession):
  stmt = (
    update(User)
    .where(User.user_id == user_id)
    .values(user_lang=lang)
  )

  await session.execute(stmt)
  await session.commit()