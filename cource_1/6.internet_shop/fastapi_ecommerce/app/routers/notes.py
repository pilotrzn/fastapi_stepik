from fastapi import APIRouter


# Создаём маршрутизатор с префиксом и тегом
router = APIRouter(
    prefix="/notes",
    tags=["notes"],
)


@router.get("/")
async def get_all_notes():
    return "Notes API is working"
