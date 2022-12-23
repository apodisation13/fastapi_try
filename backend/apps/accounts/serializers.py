from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(..., max_length=64)
    email: EmailStr
    password: str
