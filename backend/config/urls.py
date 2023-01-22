from fastapi import APIRouter

from apps.accounts.urls import router as r1
from apps.core.urls import router as r2
from apps.cards.urls import router as r3

api_router = APIRouter(prefix="/api/v1")  # глобальный префикс
api_router.include_router(r1, prefix="/users", tags=["users"])
api_router.include_router(r2, prefix="/factions", tags=["factions"])
api_router.include_router(r3, tags=["cards"])
