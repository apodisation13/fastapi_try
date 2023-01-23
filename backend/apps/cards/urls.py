from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.cards.serializers import CardsList, CreateCard, ListDecks, CreateDeck
from apps.cards.views import list_cards, create_card, list_decks, create_deck, delete_deck
from db.session import get_db

router = APIRouter()


@router.get("/cards", response_model=List[CardsList])
def get_cards(db: Session = Depends(get_db)):
    return list_cards(db)


@router.post("/cards", response_model=CardsList)
def create_new_card(card: CreateCard, db: Session = Depends(get_db)):
    card = create_card(card=card, db=db)
    return card


@router.get("/decks", response_model=List[ListDecks])
def get_decks(db: Session = Depends(get_db)):
    return list_decks(db)


@router.post("/decks", response_model=ListDecks)
# @router.post("/decks", response_model=List[ListDecks])
def create_new_deck(deck: CreateDeck, db: Session = Depends(get_db)):
    deck = create_deck(deck=deck, db=db)
    return deck


@router.delete("/decks/{deck_id}")
def delete_d(deck_id: int, db: Session = Depends(get_db)):
    msg = delete_deck(deck_id=deck_id, db=db)
    return msg
