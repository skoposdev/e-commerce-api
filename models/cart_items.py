from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class CartItems(Base):
    __tablename__ = 'cart_items'

    cart_items_id: Mapped[int] = mapped_column(primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('carts.cart_id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.product_id'))
    quantity: Mapped[int] = mapped_column()
    carts = relationship("Cart", back_populates="cart_items")
    products = relationship("Product", back_populates="cart_items")

