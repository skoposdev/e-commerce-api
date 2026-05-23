from typing import List

from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from dependencies.dependencies import check_token
from schemas.cart_items import CartItemsResponse, CartItemsCreate, CartItemsUpdate
from services.cart_items import return_cart, add_items_to_cart, update_item_from_cart
from utils.jwt_utils import decode_jwt

router = APIRouter()

@router.get("/api/cart/items", response_model=List[CartItemsResponse])
async def return_cart_items(req: Request, session: Session = Depends(get_db)):
    try:
        id = decode_jwt(req.cookies["token"])["id"]
        return [CartItemsResponse.model_validate(item) for item in return_cart(session=session, cart_id=id)]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/cart/item", response_model=CartItemsResponse)
async def put_items_to_cart(item: CartItemsCreate, token = Depends(check_token), session: Session = Depends(get_db)):
    try:
        id = int(token.get('id'))
        return add_items_to_cart(session=session, cart_id=id, item=item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/api/cart/item/{cart_id}/{cart_item_id}", response_model=CartItemsResponse)
async def update_cart_item(cart_id: int, cart_item_id: int, item: CartItemsUpdate, token = Depends(check_token), session: Session = Depends(get_db)):
    try:
        return update_item_from_cart(session=session, cart_id=cart_id, cart_item_id=cart_item_id, item=item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))