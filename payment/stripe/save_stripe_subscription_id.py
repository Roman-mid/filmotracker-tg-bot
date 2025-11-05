from models import async_session, User
from models import User
from sqlalchemy import update

async def save_stripe_subscription_id(customer_id, subscription_id):
  async with async_session() as session:
    stmt = (
      update(User)
      .where(User.stripe_customer_id == customer_id)
      .values(
        stripe_subscription_id=subscription_id
      )
    )
    await session.execute(stmt)
    await session.commit()