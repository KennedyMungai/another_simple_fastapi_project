"""The router file for the article"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(prefix="/article", tags=['article'])


@router.post("/", response_model=ArticleDisplay)
def create_article(_request: ArticleBase, _db: Session = Depends(get_db)):
    """The API endpoint to creating articles

    Args:
        _request (ArticleBase): The template for article creation
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ArticleDisplat: The new article
    """
    return db_article.create_article(_db, _request)


@router.get("/{_id}", response_model=ArticleDisplay)
def get_article(_id: int, _db: Session = Depends(get_db)):
    return db_article.get_article(_db, _id)
