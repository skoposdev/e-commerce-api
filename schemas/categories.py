from pydantic import BaseModel

class CategoryCreate(BaseModel):
    """
    Category create schema

    Attributes:
        name: Category name string
    """
    name: str

class CategoryResponse(BaseModel):
    category_id: int
    name: str

    class Config:
        from_attributes = True