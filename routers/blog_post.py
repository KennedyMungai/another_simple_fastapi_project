"""A python script that contains the blog post endpoints"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post('/new')
async def create_post(blog: BlogModel) -> str:
    return 'ok'
