from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

# Создание подключения к БД
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# чтобы в тестах создавалась своя база
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
