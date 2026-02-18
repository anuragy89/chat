from pymongo import MongoClient
from bot.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["telegram_chatbot"]

users = db.users
groups = db.groups
memory = db.memory
