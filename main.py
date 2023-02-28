from utils import load_json, key_date

PATH = 'operations.json'

data = load_json(PATH)

data.sort(key=key_date, reverse=True)  # sorts the list by dates from the latest date
