"""Starter app for expense manager application"""
# standard imports
from datetime import datetime
# third party imports
from fastapi import FastAPI
# local imports
from data_models import Transaction, TransactionList
from db_utils import DatabaseUtils
from query import Query
from db_migrations_auto import DBMigrations

DatabaseUtils.initialize_db()

app = FastAPI()


# @app.on_event("startup")
# def startup_event():
#     DBMigrations.autogenerate_and_run()


@app.get('/summary')
def get_expense_summary():
    """
    Gives brief summary of overall income and expenses
    :return: dict: income and expense, and overall balance
    """
    all_transactions = Query.get_transactions()
    income = sum(trc['amount'] for trc in all_transactions if trc['payee'].upper() == 'HARSHITA')
    expense = sum(trc['amount'] for trc in all_transactions if trc['payer'].upper() == 'HARSHITA')
    overall = income - expense
    return {'income': income, 'expense': expense, 'overall': overall}


@app.get('/transactions')
def get_transactions(to_date=None, from_date=None):
    """
    Fetches all transactions added so far
    :param to_date: Transactions from this date onwards (inclusive) to be fetched
    :param from_date: Transactions till this date (inclusive) to be fetched
    :return: List of all transactions as per the limits
    """
    all_transactions = Query.get_transactions(from_date, to_date)
    return all_transactions


@app.post('/transaction')
def add_transaction(transaction: Transaction):
    """
    Creates a new transaction record
    :param transaction: Transaction object with payer and payee details
    :return: String message to confirm transaction
    """

    return Query.add_transaction(transaction)
