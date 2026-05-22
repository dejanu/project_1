#!/usr/bin/env bash

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"

echo "GET /health"
curl -s -o /dev/null -w "Status: %{http_code}\n" "$BASE_URL/health"

# curl http://127.0.0.1:8000/items
echo "GET /items"
curl -s -o /dev/null -w "Status: %{http_code}\n" "$BASE_URL/items"


# curl -X POST http://127.0.0.1:8000/items \
#  -H "Content-Type: application/json" \
#  -d '{"name": "Widget", "price": 9.99}'
echo "POST /items"
curl -s -w "\nStatus: %{http_code}\n" -X POST "$BASE_URL/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget", "price": 9.99}'

# curl http://127.0.0.1:8000/items/1
echo "GET /items/1"
curl -s -w "\nStatus: %{http_code}\n" "$BASE_URL/items/1"

# echo "DELETE /items/1"
# curl -s -o /dev/null -w "Status: %{http_code}\n" -X DELETE "$BASE_URL/items/1"
