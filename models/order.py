from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    status: Mapped[str] = mapped_column(default='pending')
    total_prices: Mapped[float] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    order_items = relationship("OrderItems", back_populates="orders")
    user = relationship("User", back_populates="orders")