from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


# @app.get("/user/{username}/{age}")
# async def login(
#    username: Annotated[
#        str,
#        Path(
#            min_length=3,
#            max_length=15,
#            description="Enter your username",
#            examples=["Alex"],
#        ),
#    ],
#    age: int = Path(ge=0, le=100, description="enter your age"),
# ) -> dict:
#    return {"user": username, "age": age}


# @app.get("/user/{username}")
# async def login2(
#    username: Annotated[
#        str,
#        Path(
#            min_length=3,
#            max_length=15,
#            description="Enter your username",
#            example="Avdonin",
#        ),
#    ],
#    first_name: Annotated[str | None, Query(max_length=10)] = None,
# ) -> dict:
#    return {"user": username, "Name": first_name}


@app.get("/user/{username}")
async def login(
    username: Annotated[
        str,
        Path(
            min_length=3,
            max_length=15,
            description="Enter your username",
            examples=["permin0ff"],
        ),
    ],
    first_name: Annotated[str | None, Query(max_length=10, pattern="^J|s$")] = None,
) -> dict:
    return {"user": username, "Name": first_name}
