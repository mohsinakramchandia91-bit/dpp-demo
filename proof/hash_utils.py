import hashlib
import json

def compute_hash(data_dict):
    """
    Deterministic SHA256 hash of dict
    """
    serialized = json.dumps(data_dict, sort_keys=True).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()
