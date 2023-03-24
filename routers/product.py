"""The product router code"""
from fastapi import APIRouter


router = APIRouter(prefix='/product', tags=['product'])

product = ["watch", "camera", "phone"]
