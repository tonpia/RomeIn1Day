from fastapi import FastAPI
import httpx
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    logger.info("API1 received request")
    async with httpx.AsyncClient() as client:
        response = await client.get("http://api2:8001/")
        logger.info(f"API1 received response from API2: {response.text}")
    return {"message": response.json()["message"]}
