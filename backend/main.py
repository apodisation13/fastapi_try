from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.base_class import Base
from db.session import engine
from config.settings import settings
from config.urls import api_router


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


# def create_tables():
#     Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    # create_tables()
    configure_static(app)
    include_router(app)
    return app


app = start_app()
