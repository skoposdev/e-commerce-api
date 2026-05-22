from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import engine
from models.cart import Cart
from schemas.user import UserResponse
from utils.exceptions import CartCreateError


def return_cart(user: UserResponse):
    with Session(engine) as session:
        return session.execute(select(Cart).where(Cart.user_id == user.user_id)).scalars().first()

def create_cart(user_id: int, session: Session):
    try:
        session.add(Cart(user_id=user_id))
        session.commit()
    except:
        session.rollback()
        raise CartCreateError("An error occurred while creating a cart")
