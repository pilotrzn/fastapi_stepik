from fastapi import FastAPI

app = FastAPI()


@app.get("/product")
async def detail_view(item_id: int) -> dict:
    return {"product": f"Stock number {item_id}"}
