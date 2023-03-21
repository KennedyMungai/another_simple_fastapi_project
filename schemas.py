"""File contains the logic for the schemas"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """This class acts as the template for the user data

    Args:
        BaseModel (Class): The parent class
    """
    username: str
    email: str
    password: str
