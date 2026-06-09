from fastapi import FastAPI

app = FastAPI()


@app.get("/users/admin")
async def admin() -> dict:
    return {"message": "Hello admin"}


@app.get("/users/{name}")
async def users(name: str) -> dict:
    return {"user_name": name}
