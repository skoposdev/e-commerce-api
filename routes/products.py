from typing import Any

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.product import ProductCreate, ProductResponse, ProductUpdate
from services import products
from services.products import return_all_products

router = APIRouter()

@router.get("/api/products", response_model=list[ProductResponse])
async def return_products(session: Session = Depends(get_db)) -> dict[str, Any]:
    try:
        return return_all_products(session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/product", response_model=ProductResponse)
async def create_product(product: ProductCreate, session = Depends(get_db)):
    try:
        return products.create_product(session=session, product=product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/api/product/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate, session = Depends(get_db)):
    try:
        return products.update_product(session=session, product_id=product_id, product=product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))