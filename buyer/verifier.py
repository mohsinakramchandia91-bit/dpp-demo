import os
import json
import hashlib

DPP_DIR = "data/dpp"
PROOF_DIR = "data/proof"

def verify(product_id, version):
    dpp_path = os.path.join(DPP_DIR, product_id, f"v{version}.json")
    proof_path = os.path.join(PROOF_DIR, product_id, f"v{version}.json")

    if not os.path.exists(dpp_path) or not os.path.exists(proof_path):
        return False, "Record not found"

    with open(dpp_path) as f:
        dpp_data = json.load(f)

    with open(proof_path) as f:
        proof = json.load(f)

    raw = json.dumps(dpp_data, sort_keys=True).encode()
    current_hash = hashlib.sha256(raw).hexdigest()

    if current_hash != proof["hash"]:
        return False, "HASH MISMATCH — DATA TAMPERED"

    return True, "VERIFIED — DATA AUTHENTIC"
