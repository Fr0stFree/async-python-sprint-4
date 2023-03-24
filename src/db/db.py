from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import settings


Base = declarative_base()

engine = create_async_engine(url=settings.DATABASE_DSN, echo=True, future=True)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
