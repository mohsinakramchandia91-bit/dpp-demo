import os
import json

BASE_DIR = "data/lifecycle"

def ensure_dir(product_id):
    path = os.path.join(BASE_DIR, product_id)
    os.makedirs(path, exist_ok=True)
    return path

def append_event(product_id, event_obj):
    path = ensure_dir(product_id)
    file_path = os.path.join(path, "timeline.jsonl")

    with open(file_path, "a") as f:
        f.write(json.dumps(event_obj.to_dict()) + "\n")

    return file_path

def load_timeline(product_id):
    path = os.path.join(BASE_DIR, product_id, "timeline.jsonl")
    events = []

    if not os.path.exists(path):
        return events

    with open(path) as f:
        for line in f:
            events.append(json.loads(line))

    return events
