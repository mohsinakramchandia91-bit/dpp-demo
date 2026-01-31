import os
import zipfile

def zip_audit_package(product_id, version):
    base_dir = os.path.join("data/audit_packages", product_id, f"v{version}")
    zip_path = f"data/audit_packages/{product_id}-v{version}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(base_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, base_dir)
                zipf.write(full_path, arcname)

    return zip_path
