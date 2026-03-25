database = {}


def store_value(key, value):
    database[key] = value


def get_value(key):
    if key not in database.keys():
        return None
    return database[key]


def delete_value(key):
    if key not in database.keys():
        return False
    del database[key]
    return True


def list_keys():
    return database.keys()
