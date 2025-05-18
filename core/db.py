from pymongo import MongoClient

client=MongoClient("mongodb+srv://naman:naman1470@cluster0.p8kq5.mongodb.net")
db=client["discountengine"]

userscollection=db["users"]
productscollection=db["products"]
orderscollection=db["orders"]