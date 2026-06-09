from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{name}/{age}")
async def users(name: str, age: int) -> dict:
    return {"user_name": name, "user_age": age}
