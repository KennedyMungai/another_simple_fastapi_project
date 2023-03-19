"""The entrypoint for the app"""
from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class BlogType(str, Enum):
    """The template for the blog data

    Args:
        str (_type_): A simple string argument
        Enum (_type_): An enum
    """
    short: 'short'
    story: 'story'
    howto: 'howto'


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}
