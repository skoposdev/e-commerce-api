from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from models.cart_items import CartItems
from schemas.cart_items import CartItemsCreate, CartItemsUpdate
from utils.exceptions import CartItemsCreateError, CartItemsReturnedError, CartItemsDeleteError, CartItemsUpdateError


def return_cart(session: Session, cart_id: int):
    try:
        return session.execute(select(CartItems).where(CartItems.cart_id == cart_id)).scalars().all()
    except Exception as e:
        session.rollback()
        raise CartItemsReturnedError(f"Error while retrieving items from cart: {e}")


def add_items_to_cart(session: Session, cart_id: int, item: CartItemsCreate):
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


def update_item_from_cart(session: Session, cart_id: int, cart_item_id: int, item: CartItemsUpdate):
    try:
        values = item.model_dump(exclude_none=True)
        session.execute(
            update(CartItems).where(CartItems.cart_id == cart_id, CartItems.cart_items_id == cart_item_id).values(
                **values),
        )
        session.commit()
        return session.get(CartItems, cart_item_id)
    except Exception as e:
        session.rollback()
        raise CartItemsUpdateError(f"Error while updating items from cart: {e}")


def delete_item_from_cart(cart_id: int, item_id: int, session: Session):
    try:
        session.execute(
            delete(CartItems).where(CartItems.cart_id == cart_id).where(CartItems.cart_items_id == item_id))
        session.commit()
        return return_cart(session=session, cart_id=cart_id)
    except Exception as e:
        session.rollback()
        raise CartItemsDeleteError(f"Error while deleting items from cart: {e}")
