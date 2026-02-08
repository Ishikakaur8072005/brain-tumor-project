# app/routes/trends.py
from fastapi import APIRouter
from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

load_dotenv()
newsapi = NewsApiClient(api_key=os.getenv("5b61f7e708894a949537aa7dec8b2547"))

router = APIRouter()   # ← correct

@router.get("/trends/")
def get_brain_tumor_trends():
    # your news fetching code
    ...
    return {"global_news_trends": ...}