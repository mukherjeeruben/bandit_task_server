import csv
from config import CSV_FILE_PATH
from dal.record_game_data_dal import get_user_game_data

user_ids = list()

def write_to_csv(task_type, interface_name):
    filepath = CSV_FILE_PATH + '\\' + interface_name + '_dataset.csv'
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["x_id", "choice", "outcome", "subjID"])
        for user_data in task_type:
            for game_data_key, game_data_value in user_data['game_data'].items():
                if game_data_value['action'] == 'blue':
                    choice = 1
                else:
                    choice = 2
                writer.writerow([str(str(user_data['_id'])+(game_data_key)), choice, game_data_value['reward'], user_data['user_id']])


def userdata_filer(game_data): # TODO Code to keep uniform dataset for voice and conventional task
    global user_ids
    user_ids = [row['user_id'] for row in game_data if row['interface_type'] == 'voice']


if __name__ == '__main__':
    game_data = get_user_game_data()
    task_set = sorted(set([row['interface_type'] for row in game_data]), reverse=True)
    userdata_filer(game_data)
    for task_name in task_set:
        if task_name == 'conventional':
            data = [row for row in game_data if row['interface_type'] == task_name and row['user_id'] in user_ids]
        else:
            data = [row for row in game_data if row['interface_type'] == task_name]
        write_to_csv(data, task_name)



