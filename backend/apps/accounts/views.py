from sqlalchemy.orm import Session

from apps.accounts.models import User
from apps.accounts.serializers import UserCreate
from config.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
