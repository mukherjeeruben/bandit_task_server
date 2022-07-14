from interface import mdb_execute


def get_all_game_data(query_type):
    collection = 'user_game_data'
    dataset = mdb_execute.execute('get', collection, query_type)
    return dataset


if __name__ == '__main__':
    methods = ['voice', 'conventional']
    for interface_type in methods:
        query_type = {'interface_type' : interface_type}
        x = get_all_game_data(query_type)
        print(x)