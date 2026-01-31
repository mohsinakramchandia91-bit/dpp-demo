import os
import json
from core.atomic_write import atomic_json_write
from core.file_lock import acquire_lock, release_lock
from core.read_lock import with_read_lock

INDEX_DIR = "data/index"

def ensure_index_dir():
    os.makedirs(INDEX_DIR, exist_ok=True)

def index_path(batch_id):
    return os.path.join(INDEX_DIR, f"{batch_id}.json")

def load_index(batch_id):
    path = index_path(batch_id)
    lock_name = f"index_{batch_id}"

    if not os.path.exists(path):
        return None

    def read():
        with open(path) as f:
            return json.load(f)

    return with_read_lock(lock_name, read)

def save_index(batch_id, data):
    ensure_index_dir()
    lock_name = f"index_{batch_id}"
    acquire_lock(lock_name)

    try:
        atomic_json_write(index_path(batch_id), data)
    finally:
        release_lock(lock_name)
