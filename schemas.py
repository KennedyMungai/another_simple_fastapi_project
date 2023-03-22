"""File contains the logic for the schemas"""
from pydantic import BaseModel
from typing import List


# Article inside user display
class Article(BaseModel):
    """The schema for the displayed article

    Args:
        BaseModel (Class): The parent class
    """
    title: str
    content: str
    published: bool

    class Config:
        """he configuration for the Article class"""
        orm_mode = True


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
    items: List[Article] = []

    class Config:
        """Configuration class for the UserDisplay """
        orm_mode = True
