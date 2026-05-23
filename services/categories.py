from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from models.categories import Category
from schemas.categories import CategoryCreate
from utils.exceptions import CategoryCreateError, CategoryUpdateError, CategoryDeleteError


def return_all_categories(session: Session):
    return session.execute(select(Category)).scalars().all()


def create_category(session: Session, category: CategoryCreate) -> Category:
    try:
        new_category = Category(name=category.name)
        session.add(new_category)
        session.commit()
        session.refresh(new_category)
        return new_category
    except Exception as e:
        session.rollback()
        raise CategoryCreateError(f"Error creating category: {e}")


def update_category(session: Session, category_id: int, category: CategoryCreate) -> type[Category] | None:
    try:
        session.execute(
            update(Category),
            [{"category_id": category_id, "name": category.name}]
        )
        session.commit()
        return session.get(Category, category_id)
    except Exception as e:
        session.rollback()
        raise CategoryUpdateError(f"Error updating category {category_id}: {e}")


def delete_category(session: Session, category_id: int) -> None:
    try:
        session.execute(delete(Category).where(Category.category_id == category_id))
        session.commit()
    except Exception as e:
        session.rollback()
        raise CategoryDeleteError(f"Error deleting category {category_id}: {e}")