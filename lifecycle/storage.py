import os
import json

BASE_DIR = "data/dpp"

def ensure_product_dir(product_id):
    path = os.path.join(BASE_DIR, product_id)
    os.makedirs(path, exist_ok=True)
    return path

def save_dpp(dpp_obj):
    product_path = ensure_product_dir(dpp_obj.product_id)
    file_name = f"v{dpp_obj.version}.json"
    file_path = os.path.join(product_path, file_name)

    with open(file_path, "w") as f:
        json.dump(dpp_obj.to_dict(), f, indent=2)

    return file_path
