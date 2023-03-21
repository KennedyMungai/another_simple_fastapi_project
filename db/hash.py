"""This file contains the hashing logic"""
from passlib.context import CryptContext


password_cxt = CryptContext(schemes='bcrypt', deprecated='auto')
