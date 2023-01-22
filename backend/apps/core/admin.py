from sqladmin import Admin, ModelView

from apps.core.models import Faction, Color
from db.session import engine


class UserAdmin(ModelView, model=Faction):
    column_list = [Faction.id, Faction.name]
    column_sortable_list = [Color.id]


class ColorAdmin(ModelView, model=Color):
    column_list = [f for f in Color.__mapper__.column_attrs.keys()]
