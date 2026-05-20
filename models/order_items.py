from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class OrderItems(Base):
    __tablename__ = 'order_items'

    order_items_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.order_id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.product_id'))
    quantity: Mapped[int] = mapped_column()
    unit_price: Mapped[float] = mapped_column()
    orders = relationship("Order", back_populates="order_items")
    products = relationship("Product", back_populates="order_items")