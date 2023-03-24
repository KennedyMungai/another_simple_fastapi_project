"""The product router code"""
from fastapi import APIRouter, Response


router = APIRouter(prefix='/product', tags=['product'])

products = ["watch", "camera", "phone"]


@router.get('all')
def get_all_products():
    """A dummy endpoint to get all products

    Returns:
        List: All the products
    """
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")
