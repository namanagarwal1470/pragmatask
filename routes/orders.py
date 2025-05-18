from fastapi import APIRouter, Depends,HTTPException
from core.db import orderscollection, productscollection
from models.order import OrderRequest
from core.security import get_current_user
from utils.discount import calculatediscounts
from bson import ObjectId

router = APIRouter()

@router.post("/place")
def placeorder(order:OrderRequest,currentuser:dict=Depends(get_current_user)):
    total=0
    categorycount={}
    itemsinfo=[]

    for item in order.items:
        product=productscollection.find_one({"_id":ObjectId(item.productid)})
        if not product:
            raise HTTPException(404, detail="Product not found")
        itemtotal=product["price"] * item.quantity
        total += itemtotal
        category=product["category"]
        categorycount[category]=categorycount.get(category, 0)+item.quantity
        itemsinfo.append({"productid":item.productid,"quantity": item.quantity,"price":product["price"],"category": category})

    discounts=calculatediscounts(currentuser,total,categorycount,itemsinfo)
    finalamount=total-sum(discounts.values())

    orderdoc= {
        "userid": str(currentuser["_id"]),
        "items":itemsinfo,
        "total":total,
        "discounts":discounts,
        "finalamount":finalamount
    }
    result=orderscollection.insert_one(orderdoc)
    orderdoc["_id"]=str(result.inserted_id)
    return orderdoc

@router.get("/getorders")
def getuserorders(currentuser:dict=Depends(get_current_user)):
    userid=str(currentuser["_id"])
    userorders=list(orderscollection.find({"userid":userid}))
    for order in userorders:
        order["_id"]=str(order["_id"])
    return {"orders":userorders}