from fastapi import APIRouter, Depends

from data_models import *
from query import Query
from utils import Utils

router = APIRouter(tags=['Transaction'], prefix='/transactions')


@router.get('/summary')
def get_expense_summary(user=Depends(Utils.verify_jwt_token)):
    """
    Gives brief summary of overall income and expenses
    :return: dict: income and expense, and overall balance
    """
    all_transactions = Query.get_transactions()
    income = sum(trc['amount'] for trc in all_transactions if trc['payee'].upper() == 'HARSHITA')
    expense = sum(trc['amount'] for trc in all_transactions if trc['payer'].upper() == 'HARSHITA')
    overall = income - expense
    return {'income': income, 'expense': expense, 'overall': overall}


@router.get('/')
def get_transactions(to_date=None, from_date=None, user=Depends(Utils.verify_jwt_token)):
    """
    Fetches all transactions added so far
    :param to_date: Transactions from this date onwards (inclusive) to be fetched
    :param from_date: Transactions till this date (inclusive) to be fetched
    :param user: For protecting the route by JWT
    :return: List of all transactions as per the limits
    """
    all_transactions = Query.get_transactions(from_date, to_date)
    return all_transactions


@router.post('/')
def add_transaction(transaction: Transaction, user=Depends(Utils.verify_jwt_token)):
    """
    Creates a new transaction record
    :param transaction: Transaction object with payer and payee details
    :param user: For protecting the route by JWT
    :return: String message to confirm transaction
    """

    return Query.add_transaction(transaction)
