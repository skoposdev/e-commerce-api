from pydantic import BaseModel

class UserCreateOrLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    user_id: int
    email: str

    class Config:
        from_attributes = True