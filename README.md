# Discount Engine

# ----------------------------------------------
# 📌 Overview
# ----------------------------------------------
# A FastAPI-based backend for managing users, products, orders,
# and dynamic discount logic. Supports JWT authentication and
# MongoDB for data persistence.

# ----------------------------------------------
# 🧰 Tech Stack
# ----------------------------------------------
# - FastAPI: Web framework
# - MongoDB: Database
# - PyMongo: MongoDB connector
# - python-jose: JWT-based authentication
# - Pydantic: Request/response validation

# ----------------------------------------------
# 📦 Features
# ----------------------------------------------
# - User registration and login (JWT-based)
# - Product management: Add and list products
# - Order placement with discounts
# - Discount rules:
#   - 10% off if total > ₹5000
#   - ₹500 off after 5 orders
#   - 5% off on electronics if more than 3 items


# ----------------------------------------------
# 🚀 How to Run
# ----------------------------------------------
# 1. Clone the repository:
#    git clone  https://github.com/namanagarwal1470/pragmatask.git
#    cd pragmatask
#
# 2. Create a virtual environment and activate it:
#    python -m venv venv
#    source venv/bin/activate    # Linux/macOS
#    venv\Scripts\activate       # Windows
#
# 3. Install dependencies:
#    pip install -r requirements.txt
#
# 4. Run the server:
#    uvicorn main:app --reload
#

# ----------------------------------------------
# 🔐 Authentication
# ----------------------------------------------
# - Register a user to receive a JWT token
# - Use token as Bearer in `Authorization` header
# - Protected endpoints require JWT

# ----------------------------------------------
# 🔗 API Endpoints
# ----------------------------------------------


# 🔐 Auth
# POST /auth/register
#   Form Data:
#     - username
#     - password

# POST /auth/token
#   Form Data:
#     - username
#     - password
#   → Returns JWT token

# 🛒 Products
# POST /products/
#   JSON Body:
#   {
#     "name": "Laptop",
#     "category": "electronics",
#     "price": 70000
#   }

# GET /products/all
#   → Returns list of all products

# 📦 Orders
# POST /orders/place
#   Header: Authorization: Bearer <token>
#   JSON Body:
#   {
#     "items": [
#       { "productid": "abc123","quantity": 2},
#       { "productid": "def456","quantity": 1 }
#     ]
#   }

# GET /orders/getorders
#   Header: Authorization: Bearer <token>
#   → Returns all orders of the logged-in user

# ----------------------------------------------
# 🧮 Discount Rules Summary
# ----------------------------------------------
# 1. Total > ₹5000 ⇒ 10% off
# 2. More than 5 past orders ⇒ Flat ₹500 off
# 3. >3 electronics items ⇒ 5% off electronics category

# ----------------------------------------------
# 📌 Notes
# ----------------------------------------------
# - You must be logged in to access /orders
# - Discount logic is automatically applied on placing orders
# - MongoDB must be running locally on default port
