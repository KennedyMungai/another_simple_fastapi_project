"""A file containing auth code"""
import os
from datetime import datetime, timedelta
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

_env = find_dotenv(load_dotenv())


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Creates the access token

    Args:
        data (dict): The data being used to create the token
        expires_delta (Optional[timedelta], optional): The token's expiry date. Defaults to None.

    Returns:
        str: The encoded jwt token
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
