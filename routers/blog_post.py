"""A python script that contains the blog post endpoints"""
from fastapi import APIRouter


router = APIRouter(prefix='/blog', tags=['blog'])


@router.post('/')
async def create_post():
    pass
