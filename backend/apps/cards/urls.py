from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.cards.serializers import CardsList, CreateCard
from apps.cards.views import list_cards, create_card
from db.session import get_db

router = APIRouter()


@router.get("/", response_model=List[CardsList])
def get_cards(db: Session = Depends(get_db)):
    return list_cards(db)


@router.post("/", response_model=CardsList)
def create_new_card(card: CreateCard, db: Session = Depends(get_db)):
    print(card, db, 'до')
    card = create_card(card=card, db=db)
    print(card, 'после')
    return card
