"""The entrypoint for the app"""
from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status

app = FastAPI()


class BlogType(str, Enum):
    """The template for the blog data

    Args:
        str (_type_): A simple string argument
        Enum (_type_): An enum
    """
    SHORT = 'short'
    STORY = 'story'
    HOWTO = 'howto'


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: A message for when the code is successfully executed
    """
    return {"Message": "Hello World"}


@app.get(
    "/blog/all",
    tags=['blog'],
    summary="Retrieves all blogs",
    description="An API endpoint to retrieve all blogs"
)
async def get_all_blogs(page: int = 1, page_size: Optional[int] = None) -> dict:
    """An endpoint to get all blogs

    Args:
        page (_type_): _description_
        page_size (_type_): _description_

    Returns:
        dict: A message to show successful execution of the code
    """
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get("/blog/{_id}/comments/{_comment_id}", tags=['blog', 'comment'])
async def get_blog_comment(
    _id: int,
    _comment_id: int,
    _is_valid: bool = True,
    _username: Optional[str] = None
) -> dict:
    """An endpoint for finding a comment in a blog

    Args:
        _id (int): The id of the blog
        _comment_id (int): The id of the comment

    Returns:
        dict: A message to show successful execution of the code
    """
    return {
        "message": f"blog id: {_id}, comment id: {_comment_id}, validity: {_is_valid}, username: {_username}"
    }


@app.get('/blog/type/{_type}', status_code=status.HTTP_200_OK, tags=['blog'])
async def get_blog(_type: BlogType) -> dict:
    """The endpoint to retrieve a blog of a certain type

    Args:
        type (BlogType): The class 

    Returns:
        dict: A message to show successful execution
    """
    return {"Message": f"Blog type {_type}"}
