from mongo import connection, DuplicateKeyError


def save(user):
    try:
        connection.users.insert_one(user)
        return True
    except DuplicateKeyError:
        return False


def find_all():
    return list(connection['users'].find({}))
