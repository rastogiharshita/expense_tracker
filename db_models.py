from datetime import datetime
from sqlalchemy import Column, String, Float, TIMESTAMP

from db_utils import DatabaseUtils, Base


class Transactions(Base):
    __tablename__ = 'transactions'

    payee = Column(String(length=256), primary_key=True)
    payer = Column(String(length=256), primary_key=True)
    amount = Column(Float)
    currency = Column(String(length=256))
    created_at = Column(TIMESTAMP, default=datetime.now, primary_key=True)


class Users(Base):
    __tablename__ = 'users'

    username = Column(String(length=256), primary_key=True)
    password = Column(String)
