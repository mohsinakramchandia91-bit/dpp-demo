import os
import json

DOMAIN_DIR = "data/domains"

def set_domain(company_id, domain):
    os.makedirs(DOMAIN_DIR, exist_ok=True)
    path = os.path.join(DOMAIN_DIR, f"{company_id}.json")
    with open(path, "w") as f:
        json.dump({"domain": domain}, f)

def get_domain(company_id):
    path = os.path.join(DOMAIN_DIR, f"{company_id}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)["domain"]
