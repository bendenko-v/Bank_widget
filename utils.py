import json
from datetime import datetime


def load_json(path: str) -> list[dict]:
    """
    Loads data from JSON

    :param path:
        path to JSON-file with transactions
    :return:
        list of dicts (one dict - one transaction)
        """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def key_date(transaction: dict) -> datetime.date:
    """
    Gets a date in string format from a transaction and return a datetime object

    :param transaction:
        dict with transaction data
    :return:
        datetime.date object with date of transaction
        if no key 'date' in dict return date '0001-01-01'
    """
    if 'date' in transaction:
        datetime_str = transaction['date'].split('T')[0]
        return datetime.strptime(datetime_str, '%Y-%m-%d')
    return datetime.fromisoformat('0001-01-01')
