"""The router file for the article"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter(prefix="/article", tags=['article'])


@router.post("/", response_model=ArticleDisplay)
def create_article(_request: ArticleBase, _db: Session = Depends(get_db)):
    return db_article.create_article(_db, _request)
