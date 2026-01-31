import os

DATA_ROOT = "data"

def tenant_root(factory_id):
    path = os.path.join(DATA_ROOT, factory_id)
    os.makedirs(path, exist_ok=True)
    return path

def tenant_path(factory_id, *parts):
    root = tenant_root(factory_id)
    path = os.path.join(root, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path
