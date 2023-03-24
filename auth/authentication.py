"""Contains an authentication endpoint"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from db.database import get_db


router = APIRouter(tags=['authentication'])


@router.post('/token')
def get_token(
    _request: OAuth2PasswordRequestForm = Depends()
    _db: Session = Depends(get_db)
):
