import os
import json
import time

ANALYTICS_DIR = "data/analytics"

def track_event(company_id, product_id, event, meta=None):
    os.makedirs(ANALYTICS_DIR, exist_ok=True)

    path = os.path.join(ANALYTICS_DIR, f"{company_id}.json")

    record = {
        "timestamp": int(time.time()),
        "company_id": company_id,
        "product_id": product_id,
        "event": event,
        "meta": meta or {}
    }

    if os.path.exists(path):
        with open(path) as f:
            data = json.load(f)
    else:
        data = []

    data.append(record)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    return record
