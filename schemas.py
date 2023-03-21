"""File contains the logic for the schemas"""
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
