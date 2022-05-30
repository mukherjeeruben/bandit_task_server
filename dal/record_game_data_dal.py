from interface import mdb_execute


def record_user_data(user_game_data_set):
    collection = 'user_game_data'
    result = mdb_execute.execute('create', collection, user_game_data_set)
    return result[0]

