from typing import List

from fastapi import APIRouter, Request, HTTPException, Depends

from dependencies.dependencies import check_token
from schemas.cart_items import CartItemsResponse, CartItemsCreate
from services.cart_items import return_cart, add_items_to_cart
from utils.jwt_utils import decode_jwt

router = APIRouter()

@router.get("/api/cart/items", response_model=List[CartItemsResponse])
async def return_cart_items(req: Request):
    try:
        id = decode_jwt(req.cookies["token"])["id"]
        return [CartItemsResponse.model_validate(item) for item in return_cart(cart_id=id)]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/cart/item", response_model=CartItemsResponse)
async def put_items_to_cart(item: CartItemsCreate, user = Depends(check_token)):
    try:
        id = int(user.get('id'))
        item_to_cart = add_items_to_cart(cart_id=id, item=item)
        return item_to_cart
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
