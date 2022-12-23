from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from apps.accounts.serializers import UserCreate
from apps.accounts.views import create_new_user
from db.session import get_db

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
