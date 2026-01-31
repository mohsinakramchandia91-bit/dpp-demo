import os
import json
import shutil

from output.audit_summary import generate_audit_summary

BASE_DIR = "data/audit_packages"

def ensure_dir(product_id, version):
    path = os.path.join(BASE_DIR, product_id, f"v{version}")
    os.makedirs(path, exist_ok=True)
    return path

def build_audit_package(dpp_obj, public_view_path, proof_path):
    package_dir = ensure_dir(dpp_obj.product_id, dpp_obj.version)

    # 1. Summary.txt
    summary_text = generate_audit_summary(dpp_obj)
    with open(os.path.join(package_dir, "summary.txt"), "w") as f:
        f.write(summary_text)

    # 2. DPP JSON
    with open(os.path.join(package_dir, "dpp.json"), "w") as f:
        json.dump(dpp_obj.to_dict(), f, indent=2)

    # 3. Public HTML
    shutil.copy(public_view_path, os.path.join(package_dir, "public.html"))

    # 4. Proof JSON
    shutil.copy(proof_path, os.path.join(package_dir, "proof.json"))

    return package_dir
