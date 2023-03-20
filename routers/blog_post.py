"""A python script that contains the blog post endpoints"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


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
    return {"data": blog}
