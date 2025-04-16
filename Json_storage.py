import json
import os

path = "D:\student.json"

def read_data():
    try:
        if not os.path.exists(path):
            return []
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"error read data: {e}")
        return []

def write_data(data):
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"error write data: {e}")
