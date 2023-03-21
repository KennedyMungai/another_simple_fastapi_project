"""This file contains the hashing logic"""
from passlib.context import CryptContext


password_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash():
    def bcrypt(self, password: str):
        return password_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        return password_cxt.verify(plain_password, hashed_password)
