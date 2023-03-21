"""The file that contains teh ORM functionality"""
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(_db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash(request.password)
    )

    _db.add(new_user)
    _db.commit()
