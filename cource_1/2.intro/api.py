from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello. FastAPI!"}


@app.get("/products/{product_id}")
async def detail_view(product_id: int) -> dict:
    return {"product": f"Stock number {product_id}"}


@app.get("/users/{name}/{age}")
async def users(name: str, age: int) -> dict:
    return {"user_name": name, "user_age": age}


@app.get("/hello/{first_name}/{last_name}")
async def welcome_user(first_name: str, last_name: str) -> dict:
    return {"user": f"Hello, {first_name} {last_name}"}


@app.get("/order/{order_id}")
async def order(order_id: int) -> dict:
    return {"id": order_id}


@app.get("/user")
async def login(username: str, age: int) -> dict:
    return {"user": username, "age": age}


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}
