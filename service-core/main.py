# python -m venv .backend-env
# .backend-env/Scripts/activate
# pip install -r service-core/requirements.txt

# docker compose up

from fastapi import FastAPI
import httpx

app = FastAPI()

SERVICE_DATABASE_URL = "http://service-database:8001"

@app.get("/")
def read_root():
    return {"message": "Service CORE is running"}

@app.get("/fetch-data")
def fetch_data():
    response = httpx.get(f"{SERVICE_DATABASE_URL}/data")
    return response.json()