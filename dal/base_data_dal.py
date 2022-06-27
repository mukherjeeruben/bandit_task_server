from interface import mdb_execute


def record_consent_data(user_consent_data):
    collection = 'basic_user_data'
    result = mdb_execute.execute('create', collection, user_consent_data)
    return result[0]