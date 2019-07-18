import json
from gfam.config import SequenceConfig
from gfam.model.sequence_model import SequencesModel


def load_data():
    """
    load json data from json file
    :return:
    """
    with open(SequenceConfig.filename, 'r') as file:
        json_data = json.load(file)
        file.close()
        return get_sequences(json_data['sequences_data']) #get_sequence(json_data)


def get_sequences(datasets):
    sequences = []
    for data in datasets:
        seq = SequencesModel(**data)
        sequences.append(seq.__dict__)
    return sequences


def get_sequence(sequence_id):
    data = load_data()
    for i in data:
        if i["sequence_id"] == sequence_id:
            return i
    else:
        return 'Not found'


def create_sequence(sequence_data):
    with open(SequenceConfig.filename, 'w') as json_file:
        data = {}
        data['sequences_data'] = sequence_data
        json.dump(data, json_file)
        json_file.close()


def del_sequence(sequence_id):
    data = load_data()
    for i in data:
        if i["sequence_id"] == sequence_id:
            data.remove(i)
            create_sequence(data)
            return 'Sequence Deleted'
    else:
        return 'Not found'


