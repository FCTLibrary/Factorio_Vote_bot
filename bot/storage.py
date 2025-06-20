import json
import os

STORAGE_FILE = "bot/messages.json"

def load_storage():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_storage(data):
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f)

def add_message(original_msg_id, forwarded_msg_id):
    data = load_storage()
    data[str(forwarded_msg_id)] = original_msg_id
    save_storage(data)

def get_original_id(forwarded_msg_id):
    data = load_storage()
    return data.get(str(forwarded_msg_id))

def remove_message(forwarded_msg_id):
    data = load_storage()
    if str(forwarded_msg_id) in data:
        del data[str(forwarded_msg_id)]
        save_storage(data)