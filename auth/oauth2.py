"""A file containing auth code"""
from fastapi.security import OAuth2PasswordBearer


oath2_schema = OAuth2PasswordBearer(tokenUrl='token')
