from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from core.db import userscollection
from core.security import SECRET_KEY, ALGORITHM

router = APIRouter()

@router.post("/register")
def register(formdata:OAuth2PasswordRequestForm=Depends()):
    existing=userscollection.find_one({"username":formdata.username})
    if existing:
        raise HTTPException(400, "user already exists")
    user={"username": formdata.username,"password":formdata.password,"orders":[]}
    userscollection.insert_one(user)
    return {"msg":"user registered successfully"}



@router.post("/token")
def login(formdata:OAuth2PasswordRequestForm=Depends()):
    user=userscollection.find_one({"username":formdata.username})
    if not user or user["password"]!=formdata.password:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    token=jwt.encode({"sub":str(user["_id"])},SECRET_KEY,algorithm=ALGORITHM)
    return {"accesstoken":token,"tokentype":"bearer"}