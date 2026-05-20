from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    category_id: int
    name: str
    description: str
    price: float
    stock: int

class ProductResponse(BaseModel):
    product_id: int
    category_id: int
    name: str
    description: str
    price: float
    stock: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True