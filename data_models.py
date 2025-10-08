"""
Module to define all request data payload structures
"""
from pydantic import BaseModel as base, RootModel, Field


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


class User(base):
    """
    User list who can be payer/payee
    """
    username: str
    password: str | None

    model_config = {'from_attributes': True}


class UserView(base):
    """
    User but with view only properties
    """
    username: str
    password: str | None = Field(exclude=True)

    model_config = {'from_attributes': True}


class UserList(RootModel[list[User]]):
    pass


class UserViewList(RootModel[list[UserView]]):
    pass
