from typing import List

from pydantic import BaseModel

from schemas.cart_items import CartItemsResponse

class CartResponse(BaseModel):
    cart_id: int
    user_id: int
    items: List[CartItemsResponse]

    class Config:
        from_attributes = True