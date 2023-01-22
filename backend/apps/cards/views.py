from sqlalchemy.orm import Session

from apps.cards.models import Card
from apps.cards.serializers import CreateCard


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
