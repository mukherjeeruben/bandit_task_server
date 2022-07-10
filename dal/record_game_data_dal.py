from interface import mdb_execute


def record_user_data(user_game_data_set):
    collection = 'user_game_data'
    result = mdb_execute.execute('create', collection, user_game_data_set)
    return result[0]


def delete_all_data():
    dataset = dict()  # Empty to delete all
    collection = 'user_game_data'
    mdb_execute.execute('delete', collection, dataset)
    collection = 'basic_user_data'
    result = mdb_execute.execute('delete', collection, dataset)
    return result[0]

