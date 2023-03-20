"""A python script that contains the blog post endpoints"""
from typing import Optional

from fastapi import APIRouter
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


@router.post('/new')
async def create_post(blog: BlogModel) -> dict:
    """The create post endpoint

    Args:
        blog (BlogModel): The blog object

    Returns:
        dict: A dict containing the blog data
    """
    return {"data": blog}
