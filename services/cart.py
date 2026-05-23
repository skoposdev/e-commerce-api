from sqlalchemy.orm import Session

from models.cart import Cart
from utils.exceptions import CartCreateError


def create_cart(user_id: int, session: Session):
    try:
        session.add(Cart(user_id=user_id))
        session.commit()
    except:
        session.rollback()
        raise CartCreateError("An error occurred while creating a cart")
