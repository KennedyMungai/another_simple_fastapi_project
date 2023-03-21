"""The file to contain the logic for the user API endpoint"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_user
from db.database import get_db
from schemas import UserBase


router = APIRouter(prefix="/user", tags=['user'])


# Create User
@router.post("/")
async def create_user(_request: UserBase, _db: Session = Depends(get_db)):
    """The create user endpoint

    Args:
        _request (UserBase): The user data
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return db_user.create_user(_db, _request)
