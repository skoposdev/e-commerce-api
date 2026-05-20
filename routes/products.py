from typing import Any

from fastapi import APIRouter, HTTPException

from schemas.product import ProductCreate, ProductResponse, ProductUpdate
from services import products
from services.products import return_all_products, create_product

router = APIRouter()

@router.get("/api/products", response_model=list[ProductResponse])
async def return_products() -> dict[str, Any]:
    try:
        return return_all_products()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/product", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    try:
        return products.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/api/product/{product_id}", response_model=ProductUpdate)
async def update_product(product_id: int, product: ProductUpdate):
    try:
        return products.update_product(product_id, product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))