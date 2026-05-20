from fastapi import APIRouter, HTTPException

from schemas.categories import CategoryCreate, CategoryResponse
from services import categories
from services.categories import return_all_categories

router = APIRouter()


@router.get("/api/categories", response_model=list[CategoryResponse])
async def return_categories():
    try:
        return return_all_categories()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/categories", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    try:
        return categories.create_category(category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/api/categories/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category: CategoryCreate):
    try:
        return categories.update_category(category_id, category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
