from interface import mdb_execute


def record_user_data():
    data = [{"unique_id": "1yrghs6w", "set_1": "Bandit_1", "set_2": "Bandit_2",'Total_Score':'1293'},
            {"unique_id": "1hdgsas4", "set_1": "Bandit_2", "set_2": "Bandit_1",'Total_Score':'854'}]
    collection = 'user_game_data'
    result = mdb_execute.execute('create', collection, data)
    return result[0]