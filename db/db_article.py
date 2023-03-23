"""The script that handles the articles """
from sqlalchemy.orm.session import Session

from db.models import DbArticle
from schemas import ArticleBase


def create_article(_db: Session, _request: ArticleBase):
    new_article = DbArticle(
        title=_request.title,
        content=_request.content,
        published=_request.published,
        creator_id=_request.creator_id
    )


def get_article(_db: Session, _id: int):
    """A function that gets articles using the id

    Args:
        _db (Session): The database session
        _id (int): The id of the article

    Returns:
        DbArticle: A template for teh article
    """
    article = _db.query(DbArticle).filter(DbArticle.id == _id).first()
    # TODO Handle errors
    return article
