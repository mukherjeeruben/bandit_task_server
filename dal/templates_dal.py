from interface import mdb_execute


def get_template_data():
    collection = 'static_templates'
    result = mdb_execute.execute('get', collection)
    return result


def create_template_data():
    data = [{'0': {'blue': -20, 'red': +40},
             '1': {'blue': +40, 'red': -60},
             '2': {'blue': +40, 'red': -60},
             '3': {'blue': +40, 'red': -60},
             '4': {'blue': +40, 'red': -60},
             '5': {'blue': +40, 'red': -60},
             '6': {'blue': +40, 'red': -60},
             '7': {'blue': +40, 'red': -60},
             '8': {'blue': +40, 'red': -60},
             '9': {'blue': +40, 'red': -60}
             }]
    collection = 'static_templates'
    result = mdb_execute.execute('create', collection, data)
    return result[0]