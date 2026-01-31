import os
import shutil

AUDIT_DIR = "data/audit_packages"

def build_audit_package(product_id, version, paths):
    base_dir = os.path.join(AUDIT_DIR, product_id, f"v{version}")
    os.makedirs(base_dir, exist_ok=True)

    shutil.copy(paths["dpp"], os.path.join(base_dir, "dpp.json"))
    shutil.copy(paths["proof"], os.path.join(base_dir, "proof.json"))
    shutil.copy(paths["public"], os.path.join(base_dir, "public.html"))
    shutil.copy(paths["qr"], os.path.join(base_dir, "qr.txt"))

    summary_path = os.path.join(base_dir, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(
            "DIGITAL PRODUCT PASSPORT – AUDIT PACKAGE\n\n"
            f"Product ID : {product_id}\n"
            f"Version    : {version}\n\n"
            "CONTENTS\n"
            "--------\n"
            "- dpp.json     : Machine-readable DPP\n"
            "- proof.json   : Cryptographic proof (hash)\n"
            "- public.html  : Buyer-facing public view\n"
            "- qr.txt       : Public access link\n\n"
            "VERIFICATION\n"
            "------------\n"
            "1. Open public.html in any browser\n"
            f"2. Verify proof:\n   python -m proof.cli {product_id} {version}\n\n"
            "NOTE\n"
            "----\n"
            "This package is immutable and read-only.\n"
        )

    return base_dir
