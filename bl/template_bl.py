

def preprocess_template_file(file_obj):
    dataset = dict()
    if file_obj.filename == 'web_steal_scheme.csv':
        dataset['template-type'] = 'conventional'
    elif file_obj.filename == 'voice_steal_scheme.csv':
        dataset['template-type'] = 'voice'
    else:
        dataset['template-type'] = 'testing'
    raw_dataset = file_obj.read().decode('cp1252').strip().split('\n')
    header = [item.strip('"') for item in raw_dataset[0].split(',')]
    raw_dataset.pop(0)
    for index, row in enumerate(raw_dataset):
        temp_dict = dict()
        temp_dict[header[0]] = row.split(',')[0]
        temp_dict[header[1]] = row.split(',')[1]
        dataset[str(index)] = temp_dict
    return dataset


def process_template_data(dataset):
    dataset[0].pop('_id', None)
    dataset[0].pop('template-type', None)
    data = dict()
    for key, value in dataset[0].items():
        data[int(key)] = {k: int(v) for (k, v) in value.items()}
    return data
