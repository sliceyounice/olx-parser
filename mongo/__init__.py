import os
from pymongo import MongoClient
connection = MongoClient(os.environ['mongostring'])['olx-parser']
users = connection.users
offers = connection.offers
