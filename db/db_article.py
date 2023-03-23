"""The script that handles the articles """
from schemas import ArticleBase
from sqlalchemy.orm.session import Session
from db.models import DbArticle


def create_article(_db: Session, _request: ArticleBase):
    pass


def get_article(_db: Session, _id: int):
    article = _db.query(DbArticle).filter(DbArticle.id == _id).first()
    # TODO Handle errors
    return article
