from fastapi import FastAPI, status
from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated

app = FastAPI()

users = []


class UserCreate(BaseModel):
    name: str
    age: Annotated[PositiveInt, Field(..., ge=18)]


class User(BaseModel):
    id: Annotated[PositiveInt, Field(..., ge=1)]
    name: Annotated[str, Field(...)]
    age: Annotated[PositiveInt, Field(..., ge=18)]


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate) -> User:
    new_user = User(id=len(users) + 1, name=user_create.name, age=user_create.age)
    users.append(new_user)
    return new_user
