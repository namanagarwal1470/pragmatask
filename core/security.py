from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.db import userscollection
from bson import ObjectId

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="auth/token")
SECRET_KEY="supersecret"
ALGORITHM ="HS256"

def get_current_user(token:str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        userid=payload.get("sub")
        if userid is None:
            raise HTTPException(status_code=401,detail="Invalid credentials")
        user=userscollection.find_one({"_id":ObjectId(userid)})
        if user is None:
            raise HTTPException(status_code=404,detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=403,detail="Token verification failed")