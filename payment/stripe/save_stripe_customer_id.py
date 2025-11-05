from models import async_session, User
from models import User
from sqlalchemy import update

async def save_stripe_customer_id(user_id, customer_id):
  async with async_session() as session:
    stmt = (
      update(User)
      .where(User.user_id == int(user_id))
      .values(
        stripe_customer_id=customer_id, 
      )
    )
    await session.execute(stmt)
    await session.commit()
    