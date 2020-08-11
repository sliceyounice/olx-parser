from mongo import connection


def find_all():
    return list(connection['offers'].find({}, {'_id': 0}))


def insert_many(offers):
    connection['offers'].insert_many(offers)