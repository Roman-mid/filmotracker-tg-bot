from sqlalchemy import update
from models import User, with_db_session
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession

@with_db_session
async def update_user_availability(user_id: int, is_available: bool, *, session: AsyncSession):

  values = {'is_active': is_available}

  if is_available:
    values['subscription_until'] = datetime.now( ) + timedelta(days=30)

  stmt = (
    update(User)
    .where(User.user_id == user_id)
    .values(**values)
  )

  await session.execute(stmt)
  await session.commit()

