from pydantic import BaseModel

class CartItemsCreate(BaseModel):
    product_id: int
    quantity: int

class CartItemsResponse(BaseModel):
    cart_items_id: int
    cart_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True