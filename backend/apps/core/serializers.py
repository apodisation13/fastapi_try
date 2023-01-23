from pydantic import BaseModel


class FactionList(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True


class TypeList(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True


class ColorList(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True
