from fastapi import FastAPI

app = FastAPI()


# @app.get("/users")
# async def users(name: str, age: int) -> dict:
#    return {"user_name": name, "user_age": age}


@app.get("/users")
async def users(name: str = "Undefined", age: int = 18) -> dict:
    return {"user_name": name, "user_age": age}


country_dict = {
    "Russia": ["Moscow", "St. Petersburg", "Novosibirsk", "Ekaterinburg", "Kazan"],
    "USA": ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"],
}


@app.get("/country/{country}")
async def list_cities(country: str, limit: int) -> dict:
    cur_country = country_dict.get(country)
    return {"country": country, "cities": cur_country[:limit]}
