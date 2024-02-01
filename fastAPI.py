from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message:", "Hello WORLD"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
async def read_item():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_item(user_id: str, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}
