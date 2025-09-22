import pandas as pd

from db_utils import DatabaseUtils
from db_models import Transactions
from data_models import Transaction, TransactionList


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

