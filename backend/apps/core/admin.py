from sqladmin import ModelView

from apps.core.models import Faction, Color, Type
from main import admin


class FactionAdmin(ModelView, model=Faction):
    column_list = [Faction.id, Faction.name]
    column_sortable_list = [Color.id]


class ColorAdmin(ModelView, model=Color):
    column_list = [f for f in Color.__mapper__.column_attrs.keys()]


class TypeAdmin(ModelView, model=Type):
    column_list = [f for f in Type.__mapper__.column_attrs.keys()]


admin.add_view(FactionAdmin)
admin.add_view(ColorAdmin)
admin.add_view(TypeAdmin)
