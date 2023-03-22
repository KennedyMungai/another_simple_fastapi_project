"""The file to contain the logic for the user API endpoint"""
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=['user'])


# Create User
@router.post("/", response_model=UserDisplay)
async def create_user(_request: UserBase, _db: Session = Depends(get_db)):
    """The create user endpoint

    Args:
        _request (UserBase): The user data
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    return db_user.create_user(_db, _request)


@router.get("/", response_model=List[UserDisplay])
async def retrieve_all_users(_db: Session = Depends(get_db)):
    """The endpoint to retrieve all the users from the database

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List: A list of users in the UserDisplay template
    """
    return db_user.retrieve_all_users(_db)


@router.get("/{_id}", response_model=UserDisplay)
async def retrieve_one_user(_id: int, _db: Session = Depends(get_db)):
    """Retrieves one user from the database

    Args:
        _id (int): The id of the user
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        user: The user of the supplied id
    """
    return db_user.retrieve_one_user(_id, _db)


@router.put("/{_id}", response_model=UserDisplay)
async def update_user(_id: int, _request: UserBase, _db: Session = Depends(get_db)):
    return db_user.update_user_data(_id, _request, _db)
