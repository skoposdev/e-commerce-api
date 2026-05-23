from sqlalchemy import select, update
from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate, ProductUpdate
from utils.exceptions import ProductCreateError, ProductUpdateError


def return_all_products(session: Session):
    return session.execute(select(Product)).scalars().all()

def create_product(session: Session, product: ProductCreate):
    try:
        new_product = Product(
            category_id=product.category_id,
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock,
        )
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        return new_product
    except Exception as e:
        session.rollback()
        raise ProductCreateError(f"Error creating product: {e}")

def update_product(session: Session, product_id: int, product: ProductUpdate):
    try:
        values = product.model_dump(exclude_none=True)
        session.execute(
            update(Product).where(Product.product_id == product_id).values(**values)
        )
        session.commit()
        return session.get(Product, product_id)
    except Exception as e:
        session.rollback()
        raise ProductUpdateError(f"Error updating product: {e}")