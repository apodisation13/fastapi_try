from typing import Union

from fastapi import FastAPI

from apps.accounts.models import CustomUser

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/users/")
async def post_user(user: CustomUser):
    return user


@app.get("/users/")
async def get_users():
    ...
