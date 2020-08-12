from decouple import config
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
connection = MongoClient(config('mongostring'))['olx-parser']
connection['users'].create_index([('chatId', ASCENDING)], unique=True)
