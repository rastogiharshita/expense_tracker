from fastapi import APIRouter, HTTPException, status, Depends
from passlib.context import CryptContext

from data_models import *
from query import Query
from utils import Utils

router = APIRouter(tags=['User'], prefix='/users')
pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


@router.post('/')
def add_users(user: User = Depends(Utils.verify_jwt_token)):
    user.password = pwd_context.hash(user.password)
    return Query.add_user(user)


@router.get('/')
def get_users(user=Depends(Utils.verify_jwt_token)):
    return Query.get_users()


@router.post('/login')
def login(user: User):
    found_user = next(iter(Query.get_users(user, view_only=False)), None)
    if not found_user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Username not found !')
    if not pwd_context.verify(user.password, found_user['password']):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid password !')

    # generate jwt token
    access_token = Utils.generate_jwt_token_for_user(user.username)

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.delete('/')
def delete_users(user: str = Depends(Utils.verify_jwt_token)):
    return Query.delete_user(user)
