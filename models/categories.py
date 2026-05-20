from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    products = relationship("Product", back_populates="categories")