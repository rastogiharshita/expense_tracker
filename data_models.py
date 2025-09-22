"""
Module to define all request data payload structures
"""
from pydantic import BaseModel as base, RootModel


class Transaction(base):
    """
    Transaction object holding payer, payee and amt information
    """
    payee: str
    payer: str
    amount: float
    currency: str

    model_config = {"from_attributes": True}


class TransactionList(RootModel[list[Transaction]]):
    pass
