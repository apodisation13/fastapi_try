from sqlalchemy.orm import Session

from apps.core.models import Faction


def list_factions(db: Session):
    factions = db.query(Faction).all()
    return factions
