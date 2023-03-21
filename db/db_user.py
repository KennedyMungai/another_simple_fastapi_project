"""The file that contains teh ORM functionality"""
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

hash = Hash()


def create_user(_db: Session, _request: UserBase) -> DbUser:
    """A function to create a user

    Args:
        _db (Session): The database session
        _request (UserBase): The user data

    Returns:
        DbUser: A new user is created
    """
    new_user = DbUser(
        username=_request.username,
        email=_request.email,
        password=Hash.bcrypt(hash, _request.password)
    )

    _db.add(new_user)
    _db.commit()
    _db.refresh(new_user)
    return new_user
