"""A python script that contains the blog post endpoints"""
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    pass


@router.post('/new')
async def create_post():
    pass
