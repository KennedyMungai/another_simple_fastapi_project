"""The file that contains teh ORM functionality"""
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(_db: Session, _request: UserBase) -> DbUser:
    new_user = DbUser(
        username=_request.username,
        email=_request.email,
        password=Hash(_request.password)
    )

    _db.add(new_user)
    _db.commit()
    _db.refresh(new_user)
    return new_user
