from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Product(Base):
    """
    category_id: ForeignKey to Category table\n
    1 = Electronics\n
    2 = Clothes\n
    3 = Foods\n
    4 = Home and Garden\n
    5 = Sports\n
    6 = Books\n
    name: Product name [string]\n
    description: Product description [string]\n
    price: Product price [float]\n
    stock: Product stock [integer]\n
    created_at: Product creation [datetime]\n
    """
    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'))
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    stock: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    categories = relationship("Category", back_populates="products")
    cart_items = relationship("CartItems", back_populates="products")
    order_items = relationship("OrderItems", back_populates="products")
