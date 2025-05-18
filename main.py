from fastapi import FastAPI
from routes import auth, products, orders

app = FastAPI()

app.include_router(auth.router,prefix="/auth")
app.include_router(products.router,prefix="/products")
app.include_router(orders.router,prefix="/orders")
