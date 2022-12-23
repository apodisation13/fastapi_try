from fastapi import APIRouter

from apps.accounts.urls import router

api_router = APIRouter()
api_router.include_router(router, prefix="/users", tags=["users"])
