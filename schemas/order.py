from typing import List
from datetime import datetime

from pydantic import BaseModel

from schemas.order_items import OrderItemsCreate, OrderItemsResponse


class OrderCreate(BaseModel):
    items: List[OrderItemsCreate]

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    status: str
    total_price: float
    created_at: datetime
    items: List[OrderItemsResponse]

    class Config:
        from_attributes = True