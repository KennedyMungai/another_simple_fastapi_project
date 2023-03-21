"""This file contains the hashing logic"""
from passlib.context import CryptContext


password_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash():
    def bcrypt(password: str):
        return password_cxt.hash(password)
