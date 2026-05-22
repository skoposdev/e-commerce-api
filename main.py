# uvicorn main:app --reload
from fastapi import FastAPI
from routes.categories import router as categories_router
from routes.products import router as products_router
from routes.auth import router as auth_router
from routes.cart_items import router as cart_items_router

from models.user import User
from models.order import Order
from models.order_items import OrderItems
from models.cart import Cart
from models.cart_items import CartItems
from models.product import Product
from models.categories import Category

app = FastAPI()
app.include_router(categories_router, tags=["categories"])
app.include_router(products_router, tags=["products"])
app.include_router(auth_router, tags=["auth"])
app.include_router(cart_items_router, tags=["cart_items"])

