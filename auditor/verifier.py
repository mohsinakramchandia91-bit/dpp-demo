import json
import os
from proof.hash_utils import compute_hash


def verify_dpp(product_id, version):
    dpp_path = os.path.join("data", "dpp", product_id, f"v{version}.json")
    proof_path = os.path.join("data", "proof", product_id, f"v{version}.json")

    if not os.path.exists(dpp_path):
        return False, "DPP file not found"

    if not os.path.exists(proof_path):
        return False, "Proof file not found"

    with open(dpp_path) as f:
        dpp_data = json.load(f)

    with open(proof_path) as f:
        proof_data = json.load(f)

    computed = compute_hash(dpp_data)
    stored = proof_data.get("hash")

    if computed != stored:
        return False, "HASH MISMATCH – DPP TAMPERED"

    return True, "DPP VALID – HASH VERIFIED"
