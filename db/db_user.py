"""The file that contains teh ORM functionality"""
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

_new_hash = Hash()


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
        password=Hash.bcrypt(_new_hash, _request.password)
    )

    _db.add(new_user)
    _db.commit()
    _db.refresh(new_user)
    return new_user


def retrieve_all_users(_db: Session):
    """Retrieves all the users from the database

    Args:
        _db (Session): The database session

    Returns:
        _type_: All the data in the database
    """
    return _db.query(DbUser).all()


def retrieve_one_user(_id: int, _db: Session):
    """Returns a user with the supplied id

    Args:
        _id (int): The id of the user
        _db (Session): The database

    Returns:
        _type_: The user
    """
    return _db.query(DbUser).filter(DbUser.id == _id).first()


def update_user_data(_id: int, _request: UserBase, _db: Session):
    """The user update function

    Args:
        _id (int): The id of the user in the database
        _request (UserBase): The new user data
        _db (Session): The database session
    """
    user = _db.query(DbUser).filter(_request.id == _id).first()

    user.update({
        user.username: _request.username,
        user.password: _request.password,
        user.email: Hash.bcrypt(_new_hash, _request.password)
    })
