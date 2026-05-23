from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies.dependencies import check_token
from services.order import checkout
from database.database import get_db

router = APIRouter()

@router.post("/api/order")
async def init_order(session: Session = Depends(get_db), user = Depends(check_token)):
    try:
        user_id = int(user.get('id'))
        return checkout(session=session, user_id=user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))