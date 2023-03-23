"""The entrypoint for the app"""
from fastapi import FastAPI

from db import models
from db.database import engine
from routers import article, blog_get, blog_post, user

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}


app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

models.Base.metadata.create_all(engine)
