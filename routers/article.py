"""The router file for the article"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db


router = APIRouter(prefix="/article", tags=['article'])
