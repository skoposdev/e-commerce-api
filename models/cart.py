from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Cart(Base):
    __tablename__ = 'carts'

    cart_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user = relationship("User", back_populates="carts")
    cart_items = relationship("CartItems", back_populates="carts")
