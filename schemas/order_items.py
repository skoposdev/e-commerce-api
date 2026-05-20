from pydantic import BaseModel

class OrderItemsCreate(BaseModel):
    product_id: int
    quantity: int

class OrderItemsResponse(BaseModel):
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float

    class Config:
        from_attributes = True