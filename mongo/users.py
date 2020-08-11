from mongo import connection


def save(user):
    connection.users.insert_one(user)


def find_all():
    return list(connection['users'].find({}))
