from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Items API")

db: dict[int, dict] = {}
counter = 0


class Item(BaseModel):
    name: str
    price: float


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Items API</title></head>
    <body>
        <h1>Items API</h1>
        <form action="/items" method="post"
              onsubmit="event.preventDefault(); submitForm()">
            <label>Name: <input type="text" id="name" required></label><br><br>
            <label>Price: <input type="number" id="price" step="0.01" required></label><br><br>
            <button type="submit">Add Item</button>
        </form>
        <pre id="result"></pre>
        <script>
            async function submitForm() {
                const res = await fetch('/items', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        name: document.getElementById('name').value,
                        price: parseFloat(document.getElementById('price').value)
                    })
                });
                const data = await res.json();
                document.getElementById('result').textContent = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

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
