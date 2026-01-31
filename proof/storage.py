import os
import json
from datetime import datetime

BASE_DIR = "data/proof"

def ensure_dir(product_id):
    path = os.path.join(BASE_DIR, product_id)
    os.makedirs(path, exist_ok=True)
    return path

def save_proof(product_id, version, hash_value):
    product_path = ensure_dir(product_id)

    record = {
        "product_id": product_id,
        "version": version,
        "hash": hash_value,
        "timestamp": datetime.utcnow().isoformat()
    }

    file_path = os.path.join(product_path, f"v{version}.json")

    with open(file_path, "w") as f:
        json.dump(record, f, indent=2)

    return file_path
