from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Items API")

db: dict[int, dict] = {}
counter = 0


class Item(BaseModel):
    name: str
    price: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return list(db.values())


@app.post("/items", status_code=201)
def create_item(item: Item):
    global counter
    counter += 1
    db[counter] = {"id": counter, **item.model_dump()}
    return db[counter]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]