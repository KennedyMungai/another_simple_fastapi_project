"""The file that contains teh ORM functionality"""
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


def create_user(_db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=request.password,
    )
