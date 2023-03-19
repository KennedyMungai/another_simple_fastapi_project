"""The entrypoint for the app"""
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class BlogType(str, Enum):
    """The template for the blog data

    Args:
        str (_type_): A simple string argument
        Enum (_type_): An enum
    """
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}


@app.get('/blog/type/{_type}')
async def get_blog(_type: BlogType) -> dict:
    """The endpoint to retrieve a blog of a certain type

    Args:
        type (BlogType): The class 

    Returns:
        dict: A message to show successful execution
    """
    return {"Message": f"Blog type {_type}"}
