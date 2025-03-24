from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

app = FastAPI()

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="db"
)
cursor = conn.cursor()

# Type safety with Pydantic
class Item(BaseModel):
    id: int
    name: str

@app.get("/data")
def get_data():
    cursor.execute("SELECT * FROM items")
    print("Fetching data from database")
    print(cursor.fetchall())
    result = cursor.fetchall()
    return {"data": result}