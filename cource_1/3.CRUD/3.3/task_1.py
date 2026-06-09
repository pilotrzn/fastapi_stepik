from fastapi import FastAPI
from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated

app = FastAPI()


class Task(BaseModel):
    id: Annotated[PositiveInt, Field(...)]
    title: Annotated[str, Field(...)]
    completed: Annotated[bool, Field(...)]


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False),
]


@app.get("/tasks", response_model=list[Task])
async def get_tasks() -> list[Task]:
    return tasks
