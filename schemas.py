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


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
