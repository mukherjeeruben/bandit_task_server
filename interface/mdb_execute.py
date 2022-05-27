from connection.mongodb_connect import create_connection
import config


def execute(query_type, collection_name, data=None):
    result_set = list()
    client = create_connection()
    database = client.get_database(config.MONGODB_DATABASE)
    if query_type == 'get':
        db_collection = database[collection_name]
        for row_item in db_collection.find():
            result_set.append(row_item)
    elif query_type == 'create':
        db_collection = database[collection_name].insert_many(data)
        result_set.append(db_collection.acknowledged)
    return result_set

