from interface import mdb_execute


def get_template_data():
    collection = 'static_templates'
    result = mdb_execute.execute('get', collection)
    return result


def create_template_data():
    data = [{"name": "Piyush"}, {"name": "Ruben"}]
    collection = 'static_templates'
    result = mdb_execute.execute('create', collection, data)
    return result[0]