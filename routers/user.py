"""The file to contain the logic for the user API endpoint"""
from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=['user'])
