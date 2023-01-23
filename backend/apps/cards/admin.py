from sqladmin import ModelView

from apps.cards.models import Card, Deck
from main import admin


class CardAdmin(ModelView, model=Card):
    column_list = ["id", "name", "faction", "type"]
    column_sortable_list = [Card.id]


class DeckAdmin(ModelView, model=Deck):
    column_list = ["id", "name", "description", "cards"]


admin.add_view(CardAdmin)
admin.add_view(DeckAdmin)
