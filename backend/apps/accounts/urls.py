from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from apps.accounts.serializers import UserCreate, UserCreateResponse
from apps.accounts.views import create_new_user, list_users
from db.session import get_db

router = APIRouter()


@router.post("/", response_model=UserCreateResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.get("/", response_model=List[UserCreateResponse])
def get_users(db: Session = Depends(get_db)):
    return list_users(db)
