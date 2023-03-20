"""The entrypoint for the app"""
from fastapi import FastAPI

from routers import blog_get

app = FastAPI()

app.include_router(blog_get.router)


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}
