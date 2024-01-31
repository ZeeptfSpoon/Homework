from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message:", "Hello WORLD"}


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
