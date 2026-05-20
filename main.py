# uvicorn main:app --reload
from fastapi import FastAPI
from routes.categories import router as categories_router
from routes.products import router as products_router

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

