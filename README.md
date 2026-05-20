# project_1

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/) for managing items, backed by an in-memory store.

Task board [here](https://github.com/users/dejanu/projects/5)

Git commands cheatsheet [here](https://dejanu.github.io/cheeatos/git.html)
## Requirements

- Python >= 3.10
- fastapi >= 0.111.0
- uvicorn[standard] >= 0.29.0

## Running the server

```bash
uv sync
uv run uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/items` | List all items |
| `POST` | `/items` | Create a new item |
| `GET` | `/items/{item_id}` | Get an item by ID |
| `DELETE` | `/items/{item_id}` | Delete an item by ID |

### Item schema

```json
{
  "name": "string",
  "price": 0.0
}
```

## Interactive docs

Once the server is running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`


## Artifact Distribution

* GHCR: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
