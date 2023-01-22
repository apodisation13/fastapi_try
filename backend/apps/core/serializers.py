from pydantic import BaseModel


class FactionList(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True

    def __str__(self):
        return f"{self.id} - {self.name}"


class TypeList(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True

    def __str__(self):
        return f"{self.id} - {self.name}"
