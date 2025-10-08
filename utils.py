"""
General Purpose utility modules with miscellaneous helper functions
"""

import json
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

auth_scheme = OAuth2PasswordBearer(tokenUrl='user/login')


class Utils:
    """
    exportable class with miscellaneous helper functions
    """

    @staticmethod
    def get_config(file="config.json"):
        """
        Reads Config.json
        :param file: name of the config file
        :return: dict: contents of the config file
        """
        with open(file, encoding='utf-8') as config_file:
            return json.load(config_file)

    @staticmethod
    def generate_jwt_token_for_user(username: str):
        config = Utils.get_config()
        payload = {'username': username,
                   'exp': datetime.now() + timedelta(minutes=config['jwt']['expiry_in_minutes'])}
        jwt_token = jwt.encode(payload, config['jwt']['secret_key'], algorithm='HS256')
        return jwt_token

    @staticmethod
    def verify_jwt_token(token: str = Depends(auth_scheme)):
        config = Utils.get_config()
        try:
            payload = jwt.decode(token, config['jwt']['secret_key'], algorithm='HS256')
            return payload['username']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Authentication Token expired !')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Invalid Auth token ! You are not authorized for this request')
