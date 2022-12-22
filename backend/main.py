from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db.base_class import Base
from db.session import engine
from config.settings import settings


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    configure_static(app)
    create_tables()
    return app


app = start_app()
