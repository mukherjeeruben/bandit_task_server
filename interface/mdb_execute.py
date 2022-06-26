from connection.mongodb_connect import create_connection
import config


def execute(query_type, collection_name, data=None):
    result_set = list()
    client = create_connection()
    try:
        database = client.get_database(config.MONGODB_DATABASE)
        if query_type == 'get':
            db_collection = database[collection_name]
            for row_item in db_collection.find(data):
                result_set.append(row_item)
        elif query_type == 'create':
            db_collection = database[collection_name].insert_many(data)
            result_set.append(db_collection.acknowledged)
        elif query_type == 'delete':
            db_collection = database[collection_name].delete_many(data)
            result_set.append(db_collection.acknowledged)
        return result_set
    except Exception as errmsg:
        print('Error in executing query: ' + str(errmsg))
        return None

