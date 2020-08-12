from decouple import config
from pymongo import MongoClient
connection = MongoClient(config('mongostring'))['olx-parser']
