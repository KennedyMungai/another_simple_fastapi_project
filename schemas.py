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
    """The template for the data returned from the database to the front end application

    Args:
        BaseModel (Class): The parent class for the UserDisplay class
    """
    username: str
    email: str

    class Config:
        """Configuration class for the UserDisplay """
        orm_mode = True
