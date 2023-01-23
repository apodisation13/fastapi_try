from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload, contains_eager

from apps.cards.models import Card, Deck, CardDeck
from apps.cards.serializers import CreateCard, CreateDeck


def list_cards(db: Session):
    cards = db.query(Card).\
        options(
            joinedload(Card.faction),
            joinedload(Card.color),
            joinedload(Card.type),
        ).\
        all()
    return cards


def create_card(card: CreateCard, db: Session):
    card = Card(
        name=card.name,
        faction_id=card.faction_id,
        type_id=card.type_id,
    )
    db.add(card)
    db.commit()
    return card


def list_decks(db: Session):
    decks = db.query(Deck).join(CardDeck, Card).options(
        # joinedload(Card.faction),
    ).all()
    return decks


def create_deck(deck: CreateDeck, db: Session):
    cards = deck.cards
    deck = Deck(
        name=deck.name,
        description=deck.description,
    )
    db.add(deck)
    db.commit()
    for card_id in cards:
        carddeck = CardDeck(
            deck_id=deck.id,
            card_id=card_id,
        )
        db.add(carddeck)
    db.commit()
    return deck
    # return list_decks(db)


def delete_deck(deck_id: int, db: Session):
    print(deck_id)
    deck = db.get(Deck, deck_id)
    if not deck:
        raise HTTPException(status_code=404, detail="Deck not found")
    db.delete(deck)
    db.commit()
    return {"ok": 204}
