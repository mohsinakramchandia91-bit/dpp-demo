from normalization.merger import merge_field
from normalization.batch_loader import load_batch
from normalization.batch_index import load_index, save_index

def aggregate_batch(factory_id, batch_id):
    snapshots = load_batch(factory_id, batch_id)
    if not snapshots:
        return {}

    index = load_index(f"{factory_id}_{batch_id}")
    if index and index.get("last_count") == len(snapshots):
        return index["batch_view"]

    batch_view = {}
    for snap in snapshots:
        for field, data in snap.items():
            if field not in batch_view:
                batch_view[field] = data
            else:
                batch_view[field] = merge_field(batch_view[field], data)

    save_index(
        f"{factory_id}_{batch_id}",
        {
            "last_count": len(snapshots),
            "batch_view": batch_view
        }
    )
    return batch_view
