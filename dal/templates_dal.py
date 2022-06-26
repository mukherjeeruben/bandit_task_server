from interface import mdb_execute
from bl.template_bl import process_template_data


def get_template_data(templatetype):
    query = {'template-type': templatetype}
    collection = 'static_templates'
    dataset = mdb_execute.execute('get', collection, query)
    result = process_template_data(dataset)
    return result


def create_template_data(dataset):
    data = list()
    data.append(dataset)
    collection = 'static_templates'
    result = mdb_execute.execute('create', collection, data)
    return result[0]