import os

BASE_DATA = "data"

def company_paths(company_id):
    base = os.path.join(BASE_DATA, company_id)

    paths = {
        "root": base,
        "public": os.path.join(base, "public"),
        "proof": os.path.join(base, "proof"),
        "audit": os.path.join(base, "audit_packages"),
        "qr": os.path.join(base, "qr"),
        "dpp": os.path.join(base, "dpp")
    }

    for p in paths.values():
        os.makedirs(p, exist_ok=True)

    return paths
