from typing import Annotated

from fastapi import Cookie, HTTPException

from utils.jwt_utils import decode_jwt


async def check_token(token: Annotated[str | None, Cookie()]):
    if token is None:
        raise HTTPException(status_code=400, detail="Invalid token")
    try:
        user_jwt = decode_jwt(token)
        return user_jwt
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))