import os

BASE_DIR = "data/dpp"

def next_version(product_id):
    product_path = os.path.join(BASE_DIR, product_id)

    if not os.path.exists(product_path):
        return 1

    versions = []
    for f in os.listdir(product_path):
        if f.startswith("v") and f.endswith(".json"):
            try:
                versions.append(int(f[1:-5]))
            except:
                pass

    if not versions:
        return 1

    return max(versions) + 1
