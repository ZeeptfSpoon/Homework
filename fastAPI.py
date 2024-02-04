from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

def start_server():
    # print('Starting Server...')

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="debug",
        reload=True,
    )

app = FastAPI()


@app.get("/")
async def root():
    return {"message:", "Hello WORLD"}

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
async def read_item():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_item(user_id: str, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}


if __name__ == "__main__":
    start_server()
