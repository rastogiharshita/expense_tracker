"""Starter app for expense manager application"""
# standard imports
from datetime import datetime
# third party imports
from fastapi import FastAPI
# local imports
from data_models import *
from db_utils import DatabaseUtils
from query import Query
from routes import user, transaction

DatabaseUtils.initialize_db()

app = FastAPI(title='Expense Manager')
app.include_router(user.router)
app.include_router(transaction.router)
