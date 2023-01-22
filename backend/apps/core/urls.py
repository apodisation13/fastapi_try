from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from apps.core.serializers import FactionList
from apps.core.views import list_factions
from db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[FactionList])
def get_factions(db: Session = Depends(get_db)):
    return list_factions(db)
