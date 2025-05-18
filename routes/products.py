from fastapi import APIRouter
from core.db import productscollection
from models.product import Product


router = APIRouter()

@router.post("/")
def addproduct(product: Product):
    result=productscollection.insert_one(product.dict())
    return {"id":str(result.inserted_id)}

@router.get("/all")
def listproducts():
    return [ {**p,"_id":str(p["_id"])} for p in productscollection.find()]