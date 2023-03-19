"""The entrypoint for the app"""
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}
