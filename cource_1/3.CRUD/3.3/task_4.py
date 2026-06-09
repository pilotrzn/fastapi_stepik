from fastapi import FastAPI, status, HTTPException as he
from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated

app = FastAPI()


class User(BaseModel):
    id: Annotated[PositiveInt, Field(..., ge=1)]
    name: Annotated[str, Field(...)]
    age: Annotated[PositiveInt, Field(..., gt=0)]


class UserUpdate(BaseModel):
    name: str
    age: Annotated[PositiveInt, Field(..., gt=0)]


users: list[User] = [
    User(id=1, name="Алексей", age=25),
    User(id=2, name="Мария", age=30),
    User(id=3, name="Иван", age=22),
    User(id=4, name="Елена", age=28),
    User(id=5, name="Дмитрий", age=35),
]


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            updated_user = User(id=user_id, name=user_update.name, age=user_update.age)
            users[i] = updated_user
            return updated_user
    raise he(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
