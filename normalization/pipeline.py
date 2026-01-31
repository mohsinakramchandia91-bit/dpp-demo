from normalization.normalizer import normalize_raw_event
from normalization.storage import save_normalized_snapshot

def process_event(raw_event):
    normalized = normalize_raw_event(raw_event)
    save_normalized_snapshot(
        raw_event.factory_id,
        raw_event.batch_id,
        normalized
    )
    return normalized
