import os

from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Please explain what is data mining",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Data Miner"}

@app.get("/analyze")
async def analyze():
    return {"message": response.text}
