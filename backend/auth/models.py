
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import MetaData, Column, String, Integer

from database import get_async_session

Base: DeclarativeMeta = declarative_base()

metadata = MetaData()

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)  # type: ignore
    username = Column(String, nullable=False)
    bank = Column(Integer, nullable=False, default=1000)



async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
