"""The script that handles the articles """
from schemas import ArticleBase
from sqlalchemy.orm.session import Session


def create_article(_db: Session, _request: ArticleBase):
    pass


def get_article(_db: Session, _id: int):
    pass
