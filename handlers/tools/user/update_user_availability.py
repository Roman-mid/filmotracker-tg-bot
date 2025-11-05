from sqlalchemy import update
from models import async_session, User
from datetime import datetime, timedelta

async def update_user_availability(user_id: int, is_available: bool):
  async with async_session() as session:

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

