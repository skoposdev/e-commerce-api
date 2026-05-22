from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import engine
from models.cart import Cart
from models.user import User
from schemas.user import UserCreateOrLogin, UserResponse
from services.cart import create_cart
from utils.exceptions import UserNotFoundError, UserCreateError

def retrieve_user(user: UserCreateOrLogin):
    with Session(engine) as session:
        try:
            user = session.execute(select(User).where(User.email == user.email)).scalars().first()
            cart_id = session.execute(select(Cart).where(Cart.user_id == user.user_id)).scalars().first()

            if not cart_id:
                create_cart(user.user_id, session)

            return session.execute(select(User).where(User.email == user.email)).scalars().first()
        except Exception as e:
            raise UserNotFoundError(f"Error while retrieving user: {e}")

def create_user(user: UserCreateOrLogin):
    with Session(engine) as session:
        try:
            password_hash = PasswordHash.recommended()
            hashed_password = password_hash.hash(user.password)

            inserted_user = User(
                email=user.email,
                password_hash=hashed_password,
            )

            session.add(inserted_user)
            session.commit()
            session.refresh(inserted_user)
        except:
            session.rollback()
            raise UserCreateError("Error while creating user")