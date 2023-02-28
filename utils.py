import json


def load_json(path):
    """
    Load data from JSON

    :param path: path to JSON-file with transactions
    :return: list of dicts (one dict - one transaction)
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


