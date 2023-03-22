"""A python file to define the models of the data to be put inside the database"""
from sqlalchemy import Column, Integer, String, Boolean

from db.database import Base


class DbUser(Base):
    """The template for the User data

    Args:
        Base (Function): Parent class
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class DbArticle(Base):
    """The article database model

    Args:
        Base (Function): Some function
    """
    __tablename__ = "Articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
