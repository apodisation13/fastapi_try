from sqlalchemy.orm import Session

from apps.cards.models import Card, Deck, CardDeck
from apps.cards.serializers import CreateCard, CreateDeck


def list_cards(db: Session):
    cards = db.query(Card).all()
    return cards


def create_card(card: CreateCard, db: Session):
    print(card, db, 'createcard')
    card = Card(
        name=card.name,
        faction_id=card.faction_id,
        type_id=card.type_id,
    )
    db.add(card)
    db.commit()
    return card


def list_decks(db: Session):
    decks = db.query(Deck).all()
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
