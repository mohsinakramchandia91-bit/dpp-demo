import json
import os

DATA_DIR = "data/raw_events"

def ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def save_raw_event(raw_event):
    ensure_dir()
    path = os.path.join(DATA_DIR, f"{raw_event.batch_id}.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(raw_event.to_dict()) + "\n")
