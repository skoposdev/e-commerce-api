from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import engine
from models.cart_items import CartItems
from schemas.cart_items import CartItemsCreate
from utils.exceptions import CartItemsCreateError, CartItemsReturnedError


def return_cart(cart_id: int):
    with Session(engine) as session:
        try:
            return session.execute(select(CartItems).where(CartItems.cart_id == cart_id)).scalars().all()
        except Exception as e:
            session.rollback()
            raise CartItemsReturnedError(f"Error while retrieving items from cart: {e}")

def add_items_to_cart(cart_id: int, item: CartItemsCreate):
    with Session(engine) as session:
        try:
            new_item = CartItems(
                cart_id=cart_id,
                product_id=item.product_id,
                quantity=item.quantity,
            )
            session.add(new_item)
            session.commit()
            session.refresh(new_item)
            return new_item
        except Exception as e:
            session.rollback()
            raise CartItemsCreateError(f"Error while adding items to cart: {e}")