from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from apps.core.models import Color, Faction, Type
from db.base_class import Base


class Card(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(Integer, ForeignKey(Color.id))
    faction_id = Column(Integer, ForeignKey("faction.id"))
    faction = relationship("Faction")
    type_id = Column(Integer, ForeignKey(Type.id))
    type = relationship("Type")

    def __str__(self):
        return f"{self.id} - {self.name}"
