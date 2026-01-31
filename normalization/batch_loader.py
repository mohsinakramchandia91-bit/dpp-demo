import os
import json
from core.tenant import tenant_path

def load_batch(factory_id, batch_id):
    batch_dir = tenant_path(factory_id, "normalized", batch_id)
    if not os.path.exists(batch_dir):
        return []

    snapshots = []
    for f in sorted(os.listdir(batch_dir)):
        with open(os.path.join(batch_dir, f)) as fh:
            snapshots.append(json.load(fh))
    return snapshots
