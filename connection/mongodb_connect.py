import logging
from flask_pymongo import pymongo
import config


def create_connection():
    '''Create mongodb connection object'''
    logging.basicConfig(level=logging.INFO)
    try:
        connection_string = '''mongodb+srv://'''+config.MONGODB_USER+''':'''+config.MONGODB_PASSWORD+'''@'''+config.MONGODB_CLUSTER+'''.gljli.mongodb.net/?retryWrites=true&w=majority'''
        client_con = pymongo.MongoClient(connection_string)
        logging.info('Database Connection Object Created')
        return client_con
    except Exception as msg:
        logging.error("Database Connection error: " + str(msg))
        return None
