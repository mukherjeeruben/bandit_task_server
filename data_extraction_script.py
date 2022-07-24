from interface import mdb_execute
import pandas as pd
from bson import json_util
import json
import csv

def get_all_game_data(query_type):
    collection = 'user_game_data'
    dataset = mdb_execute.execute('get', collection, query_type)
    return dataset


if __name__ == '__main__':
    method1 = ['voice']
    method2= ['conventional']
    result_df1= pd.DataFrame(columns=['X_id','interface_type','user_id','action','reward','total_score'])
    result_df2 = pd.DataFrame(columns=['X_id', 'interface_type', 'user_id', 'action', 'reward', 'total_score'])
    print(result_df2)
    for interface_type in method1:
        query_type = {'interface_type' : interface_type}
        x = get_all_game_data(query_type)
        print(x)
    for interface_type in method2:
        query_type = {'interface_type' : interface_type}
        x = get_all_game_data(query_type)
        print(len(x))
        print(x)



