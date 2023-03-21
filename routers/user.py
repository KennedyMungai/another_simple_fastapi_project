"""The file to contain the logic for the user API endpoint"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from schemas import UserBase


router = APIRouter(prefix="/user", tags=['user'])


# Create User
@router.post("/")
async def create_user(_request: UserBase, _db: Session = Depends(get_db)):
    pass
