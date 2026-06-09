from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()


profiles_dict = {
    "alex": {
        "name": "Александр",
        "age": 33,
        "phone": "+79463456789",
        "email": "alex@my-site.com",
    },
    "ustas": {
        "name": "Юстас",
        "age": 90,
        "phone": "+100",
        "email": "ustas@him-site.com",
    },
}


@app.get("/users")
async def retrieve_user_profile(
    username: Annotated[
        str, Query(min_length=2, max_length=50, description="Имя пользователя")
    ],
) -> dict:
    if username in profiles_dict:
        return profiles_dict[username]
    return {"message": f"Пользователь {username} не найден."}


@app.get("/category/{category_id}/products")
async def category(
    category_id: Annotated[int, Path(gt=0, description="Category ID")], page: int
) -> dict:
    return {"category_id": category_id, "page": page}


@app.get("/users/{name}")
async def get_user(
    name: str = Path(min_length=4, max_length=20, description="Enter your name"),
) -> dict:
    return {"user_name": name}
