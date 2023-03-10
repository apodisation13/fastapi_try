from typing import Union

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(..., max_length=64)
    email: EmailStr
    password: str


class UserCreateResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    scraps: Union[int, None]

    class Config:
        orm_mode = True
