import pandas as pd

from db_utils import DatabaseUtils
from db_models import *
from data_models import *


class Query:
    @classmethod
    def get_transactions(cls, from_date=None, to_date=None):
        with DatabaseUtils.session_scope() as session:
            sq = session.query(Transactions)
            if from_date is not None:
                sq = sq.filter(Transactions.created_at >= from_date)
            if to_date is not None:
                sq = sq.filter(Transactions.created_at <= to_date)
            results = sq.all()
            return TransactionList.model_validate(results).model_dump()

    @classmethod
    def add_transaction(cls, transaction: Transaction):
        with DatabaseUtils.session_scope() as session:
            trc = Transactions(**transaction.dict())
            session.add(trc)
        return 'Transaction added !'

    @classmethod
    def add_user(cls, user: User):
        with DatabaseUtils.session_scope() as session:
            session.add(Users(**user.dict()))
            return 'User added !'

    @classmethod
    def delete_user(cls, user: str):
        with DatabaseUtils.session_scope() as session:
            sq = session.query(Users)
            if user is not None:
                sq = sq.filter(Users.username == user)
            sq.delete(synchronize_session=False)
            return "User deleted !"

    @classmethod
    def get_users(cls, user: User | None = None, view_only=True):
        with DatabaseUtils.session_scope() as session:
            sq = session.query(Users)
            if user is not None:
                sq = sq.filter(Users.username == user.username)
            results = sq.all()
            if view_only:
                return UserViewList.model_validate(results).model_dump()
            else:
                return UserList.model_validate(results).model_dump()
