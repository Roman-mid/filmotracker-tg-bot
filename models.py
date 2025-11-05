
from sqlalchemy import Column, BigInteger, DateTime, Boolean, Integer, String, Date, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date
from config import DATABASE_URL

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    user_lang = Column(String, nullable=False)
    user_name = Column(String, nullable=True)
    subscription_until = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    stripe_customer_id = Column(String, nullable=True)
    stripe_subscription_id = Column(String, nullable=True)
    createdAt = Column(DateTime, default=date.today())


class UserMovie(Base):
    __tablename__ = "user_movies"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    movie_id = Column(BigInteger)
    title = Column(String)
    lang = Column(String, nullable=True)
    movie_type = Column(String)
    next_release_date = Column(Date, nullable=True)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
