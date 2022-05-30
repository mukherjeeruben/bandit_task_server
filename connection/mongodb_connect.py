from flask_pymongo import pymongo
import config


def create_connection():
    try:
        connection_string = '''mongodb+srv://'''+config.MONGODB_USER+''':'''+config.MONGODB_PASSWORD+'''@'''+config.MONGODB_CLUSTER+'''.gljli.mongodb.net/?retryWrites=true&w=majority'''
        client_con = pymongo.MongoClient(connection_string)
        return client_con
    except Exception as msg:
        print('Error in creating connection object: ' + str(msg))
        return None
