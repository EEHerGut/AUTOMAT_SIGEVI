import json
from pathlib import Path

def load_json(file_name):
    data_path = Path(__file__).parent.parent / "data" / file_name
    with open(data_path, 'r', encoding='utf-8') as file:
        return json.load(file)