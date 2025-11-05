from models import async_session, User
from models import User
from sqlalchemy import select

async def get_user_by_stripe_customer_id(customer_id) -> User | None:
  async with async_session() as session:
    user = await session.execute(
      select(User)
      .where(User.stripe_customer_id == customer_id)
    )

    return user.scalar_one_or_none()