from fastapi import FastAPI, Depends, HTTPException
from starlette import status

app = FastAPI()


async def check_auth(token: str):
    if token == "secret":
        return "User is authorized"
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


@app.get("/profile")
async def check_profile_auth(check: bool = Depends(check_auth)):
    return check
