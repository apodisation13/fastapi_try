from typing import Optional, List

from pydantic import BaseModel, root_validator, Field, validator

from apps.core.serializers import FactionList, TypeList, ColorList


class CardsList(BaseModel):
    id: int
    name: str = Field(alias='neeeeeeeeee')  # ЭТО ЕСЛИ надо переименовать какое-то поле на neeeeeeeee
    faction: FactionList
    type: TypeList
    color: ColorList
    # non_existent_field: int = 1  # это если добавить как-то вообще кастомное поле

    class Config:
        orm_mode = True
        allow_population_by_field_name = True  # это надо чтобы можно было юзать алиас

    @validator('type')
    def type_(cls, t):
        return t.name

    @validator('faction')
    def faction_(cls, f):
        return f.name

    @validator('color')
    def color_(cls, c):
        return c.name

    # ЕЩЁ СПОСОБЫ
    # def from_orm(cls, *args, **kwargs):
    #     print(cls)
    #     return { "a": "b" }

    # def dict(self, *args, **kwargs):
    #     print(type(self))
    #     return {"id": self.id, "name": self.name, "faction": self.faction.name}

    # И ЕЩЁ СПОСОБ, кстати крутой, тут вообще все values, аналог to_representation
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
