"""The script that handles the articles """
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbArticle
from exceptions import StoryException
from schemas import ArticleBase


def create_article(_db: Session, _request: ArticleBase):
    """The create article function

    Args:
        _db (Session): The database session
        _request (ArticleBase): The template for the nw article data

    Returns:
        ArticleBase: The newly created article
    """
    if _request.content.startswith("Once upon a time"):
        raise StoryException("No stories oplease")

    new_article = DbArticle(
        title=_request.title,
        content=_request.content,
        published=_request.published,
        creator_id=_request.creator_id
    )

    _db.add(new_article)
    _db.commit()
    _db.refresh(new_article)

    return new_article


def get_article(_db: Session, _id: int):
    """A function that gets articles using the id

    Args:
        _db (Session): The database session
        _id (int): The id of the article

    Returns:
        DbArticle: A template for teh article
    """
    article = _db.query(DbArticle).filter(DbArticle.id == _id).first()

    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The article with the id of {_id} was not found"
        )

    return article
