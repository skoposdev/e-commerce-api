from fastapi import APIRouter, Response, HTTPException
from pwdlib import PasswordHash
from starlette import status

from schemas.user import UserCreateOrLogin, UserResponse
from services.auth import retrieve_user, create_user
from utils.exceptions import UserNotFoundError
from utils.jwt_utils import create_token

router = APIRouter()

@router.post("/auth/login", response_model=UserResponse)
async def login(res: Response, user_login: UserCreateOrLogin):
    try:
        user = retrieve_user(user_login)
        password_hash = PasswordHash.recommended()

        if password_hash.verify(user_login.password, user.password_hash):
            token = create_token(user.user_id)
            res.set_cookie("token", value=token, secure=False, httponly=True)
            return user
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/auth/register", response_model=UserResponse)
async def register(user_register: UserCreateOrLogin):
    try:
        user = create_user(user_register)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))