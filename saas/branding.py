import os
import json

BRAND_DIR = "data/branding"

def set_branding(company_id, brand):
    os.makedirs(BRAND_DIR, exist_ok=True)
    path = os.path.join(BRAND_DIR, f"{company_id}.json")
    with open(path, "w") as f:
        json.dump(brand, f, indent=2)

def get_branding(company_id):
    path = os.path.join(BRAND_DIR, f"{company_id}.json")
    if not os.path.exists(path):
        return {
            "company_name": "Verified Manufacturer",
            "logo": "",
            "theme_color": "#0f766e",
            "powered_by": "hidden"
        }
    with open(path) as f:
        return json.load(f)
