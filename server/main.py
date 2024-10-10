from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mongo_uri = "mongodb://mongodb:27017"
client = MongoClient(mongo_uri)
db = client["Crawler"]
collection = db["limited_edition"]

class Item(BaseModel):
    title: str
    first_model_name: str
    description_for_first_model: str

@app.get("/api/items")
def get_items():
    items = list(collection.find({}, {'_id': 0}))
    print(items)
    return items
