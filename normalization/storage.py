import os
from datetime import datetime
from core.file_lock import acquire_lock, release_lock
from core.atomic_write import atomic_json_write
from core.tenant import tenant_path

def serialize_snapshot(snapshot):
    out = {}
    for field, value in snapshot.items():
        if hasattr(value, "to_dict"):
            out[field] = value.to_dict()
        else:
            out[field] = value
    return out

def save_normalized_snapshot(factory_id, batch_id, snapshot):
    lock_name = f"norm_{factory_id}_{batch_id}"
    acquire_lock(lock_name)

    try:
        filename = datetime.utcnow().isoformat() + ".json"
        file_path = tenant_path(
            factory_id,
            "normalized",
            batch_id,
            filename
        )

        clean = serialize_snapshot(snapshot)
        atomic_json_write(file_path, clean)
        return file_path
    finally:
        release_lock(lock_name)
