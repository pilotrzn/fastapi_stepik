from fastapi import FastAPI, Depends, Query

app = FastAPI()


async def get_limit(limit: int = 10):
    return {"limit": limit}


@app.get("/items")
async def get_items(limit: dict = Depends(get_limit)):
    return {"limit": limit}
