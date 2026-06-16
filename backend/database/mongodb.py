from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("MONGO_URI"))

client = MongoClient(os.getenv("MONGO_URI"))

db = client["resume_analyzer"]