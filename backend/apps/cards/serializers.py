from typing import Optional, List

from pydantic import BaseModel, root_validator, Field, validator

from apps.core.serializers import FactionList, TypeList


class CardsList(BaseModel):
    id: int
    name: str = Field(alias='neeeeeeeeee')
    faction: FactionList
    type: TypeList
    # non_existent_field: int = 1

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

    @validator('type')
    def type_(cls, t):
        return t.name

    @validator('faction')
    def faction_(cls, f):
        return f.name

    # def from_orm(cls, *args, **kwargs):
    #     print(cls)
    #     return { "a": "b" }

    # def dict(self, *args, **kwargs):
    #     print(type(self))
    #     return {"id": self.id, "name": self.name, "faction": self.faction.name}

    # @root_validator
    # def validate_date(cls, values):
    #     # f = values.pop("faction")
    #     # t = values.pop("type")
    #     # return values | {"faction": f.name} | {"type": t.name}
    #     f = values["faction"].id
    #     t = values["type"].id
    #     print(f, t)
    #     return values | {"non_existent_field": f + t}


class CreateCard(BaseModel):
    name: str
    faction_id: int
    type_id: int


class ListDecks(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    cards: List[CardsList]

    class Config:
        orm_mode = True


class CreateDeck(BaseModel):
    name: str
    description: Optional[str] = None
    cards: List[int]
