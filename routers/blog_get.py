"""Blog get operations API router file"""
from typing import Optional

from fastapi import APIRouter, status

from main import BlogType

router = APIRouter(prefix='/blog', tags=["blog"])


@router.get(
    "/all",
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


@router.get("/{_id}/comments/{_comment_id}", tags=['blog', 'comment'])
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


@router.get('/type/{_type}', status_code=status.HTTP_200_OK, tags=['blog'])
async def get_blog(_type: BlogType) -> dict:
    """The endpoint to retrieve a blog of a certain type

    Args:
        type (BlogType): The class 

    Returns:
        dict: A message to show successful execution
    """
    return {"Message": f"Blog type {_type}"}
