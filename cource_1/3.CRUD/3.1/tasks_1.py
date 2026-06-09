from fastapi import FastAPI, status, Body, HTTPException

app = FastAPI()

goals_db = {
    0: "Learn FastAPI basics",
    1: "Build CRUD app",
    2: "Write tests with TestClient",
    3: "Add authentication",
    4: "Deploy to production",
}


@app.delete("/goals/{goal_id}", status_code=status.HTTP_200_OK)
async def delete_goal(goal_id: int) -> str:
    if goal_id not in goals_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found"
        )
    goals_db.pop(goal_id)
    return f"Goal ID={goal_id} deleted!"


quotes_db = {
    0: "FastAPI lets you build APIs fast with type hints",
    1: "Auto docs at /docs and /redoc with OpenAPI",
    2: "Pydantic validates your data",
    3: "Depends gives clean Dependency Injection",
    4: "Use async def and await for concurrency",
}


@app.put("/quotes/{quote_id}")
async def update_quote(quote_id: int, quote: str = Body(...)) -> str:
    if quote_id not in quotes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found"
        )
    quotes_db[quote_id] = quote
    return "Quote updated!"


reminders_db = {}


@app.post("/reminders", status_code=status.HTTP_201_CREATED)
async def create_reminder(reminder: str = Body(...)) -> str:
    current_index = max(reminders_db) + 1 if reminders_db else 0
    reminders_db[current_index] = reminder
    return "Reminder created!"


tasks_db = {0: "Study FastAPI", 1: "I like FastAPI"}


@app.get("/tasks/{task_id}")
async def read_task(task_id: int) -> str:
    try:
        return tasks_db[task_id]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )


notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}


@app.get("/notes")
async def get_notes() -> dict:
    return notes_db
