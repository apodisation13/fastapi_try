from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView

from apps.core.models import Faction
from config.settings import settings
from config.urls import api_router
from db.session import engine
from apps.core.admin import UserAdmin, ColorAdmin


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def include_router(app):
    app.include_router(api_router)


def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    configure_static(app)
    include_router(app)
    return app


app = start_app()
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(ColorAdmin)
