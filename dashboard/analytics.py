import os
import json

ANALYTICS_DIR = "data/analytics"

def company_analytics(company_id):
    path = os.path.join(ANALYTICS_DIR, f"{company_id}.json")

    if not os.path.exists(path):
        return []

    with open(path) as f:
        return json.load(f)
