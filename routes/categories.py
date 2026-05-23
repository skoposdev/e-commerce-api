from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from dependencies.dependencies import check_token
from schemas.categories import CategoryCreate, CategoryResponse
from services import categories
from services.categories import return_all_categories

router = APIRouter()


@router.get("/api/categories", response_model=list[CategoryResponse])
async def return_categories(session: Session = Depends(get_db), token = Depends(check_token)):
    try:
        return return_all_categories(session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/categories", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, session: Session = Depends(get_db), token = Depends(check_token)):
    try:
        return categories.create_category(session=session, category=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/api/categories/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: int, category: CategoryCreate, session: Session = Depends(get_db), token = Depends(check_token)):
    try:
        return categories.update_category(session=session, category_id=category_id, category=category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
