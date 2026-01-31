import os
import json
import hashlib
import uuid

AUTH_DIR = "data/companies"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_company(name, email, password):
    company_id = f"cmp_{uuid.uuid4().hex[:8]}"
    company_dir = os.path.join(AUTH_DIR, company_id)
    os.makedirs(company_dir, exist_ok=True)

    data = {
        "company_id": company_id,
        "name": name,
        "email": email,
        "password_hash": hash_password(password),
        "plan": "starter"
    }

    with open(os.path.join(company_dir, "company.json"), "w") as f:
        json.dump(data, f, indent=2)

    return company_id

def login(email, password):
    for cid in os.listdir(AUTH_DIR):
        path = os.path.join(AUTH_DIR, cid, "company.json")
        if not os.path.exists(path):
            continue

        with open(path) as f:
            data = json.load(f)

        if data["email"] == email and data["password_hash"] == hash_password(password):
            return data

    return None
