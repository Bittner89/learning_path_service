import os
from dotenv import load_dotenv
from typing import List, Dict, Any
from.helpers import get_json

load_dotenv()

TOPICS_API_BASE_URL = os.getenv("TOPICS_API_BASSE_URL", "http://127.0.0.1:5000").rstrip("/")
RESOURCES_API_BASE_URL = os.getenv("RESOURCES_API_BASE_URL", "http://localhost:5002").rstrip("/")

def fetch_topics():
    return get_json(f"{TOPICS_API_BASE_URL}/topics")

def fetch_skills():
    return get_json(f"{TOPICS_API_BASE_URL}/skills")

def fetch_resources():
    items = get_json(f"{RESOURCES_API_BASE_URL}/resources")

    for item in items:
        if "id" not in item and "_id" in item:
            item["id"] = str(item["id"])

    return items            


