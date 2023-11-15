from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import Column, String, Integer

Base: DeclarativeMeta = declarative_base()

class Game(Base):
    id = Column(Integer, primary_key=True)
    user_bank = Column(Integer, nullable=False, default=0)
    wager = Column(Integer, nullable=False, default=0)
    sum_users_cards = Column(Integer, nullable=False, default=0)
    sum_dealers_cards = Column(Integer, nullable=False, default=0)
    status = Column(String, nullable=False, default='begins')

