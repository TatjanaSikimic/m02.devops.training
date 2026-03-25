from datastore import get_value, store_value, delete_value as delete_value_db, list_keys

def process_and_store(key, raw_value):
    processed_value = raw_value.strip().upper()
    store_value(key, processed_value)
    return processed_value


def retrieve_processed(key):
    retrieved_value = get_value(key)
    if retrieved_value:
        return retrieved_value.lower()
    return None


def update_value(key, raw_value):
    return store_value(key, raw_value)


def delete_value(key):
    return delete_value_db(key)


def list_all_keys():
    return list_keys()
