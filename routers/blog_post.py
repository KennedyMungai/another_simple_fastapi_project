"""A python script that contains the blog post endpoints"""
from typing import List, Optional

from fastapi import APIRouter, Body, Query, Path
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    """The template for the blog data

    Args:
        BaseModel (Class): The parent class
    """
    title: str
    content: str
    published: Optional[bool]
    tags: List[str]


@router.post('/new/{_id}')
async def create_post(blog: BlogModel, _id: int, _version: int = 1) -> dict:
    """The create post endpoint

    Args:
        blog (BlogModel): The blog object

    Returns:
        dict: A dict containing the blog data
    """
    return {
        "id": _id,
        "data": blog,
        "version": _version
    }


@router.post('/new/{_id}/comments/{_comment_id}')
async def create_comment(
    blog: BlogModel,
    _id: int,
    # __comment_title: Query(
    #     None,
    #     title="Id of the comment",
    #     description="Some description for the comment_title",
    #     alias='Comment Title'
    # ),
    _content: str = Body(
        ...,
        min_length=10, max_length=80,
        regex='^[a-z\s]*$'),
    _v: Optional[List[str]] = Query(None),
        _comments_id: int = Path(gt=5, le=10)) -> dict:
    """An endpoint to create comments

    Args:
        blog (BlogModel): The template for the blog data
        _id (int): The id of the blog
        _comment_id (Query, optional): The comment of the if. Defaults to "Id of the comment", description="Some description for the comment_id").

    Returns:
        dict: _description_
    """
    return {
        "blog": blog,
        "id": _id,
        # "comment title": __comment_title,
        "content": _content,
        "version": _v
    }
