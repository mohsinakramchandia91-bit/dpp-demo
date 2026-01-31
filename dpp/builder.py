import os
import json
from datetime import datetime

DPP_DIR = "data/dpp"

class DPP:
    def __init__(self, product_id, batch_id, version, batch_view, compliance_report, factory_id):
        self.product_id = product_id
        self.batch_id = batch_id
        self.version = version
        self.factory_id = factory_id
        self.created_at = datetime.utcnow().isoformat()
        self.batch_view = batch_view
        self.compliance_report = compliance_report

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "batch_id": self.batch_id,
            "factory_id": self.factory_id,
            "version": self.version,
            "created_at": self.created_at,
            "batch_view": self.batch_view,
            "compliance_report": self.compliance_report
        }

def ensure_dir(product_id):
    path = os.path.join(DPP_DIR, product_id)
    os.makedirs(path, exist_ok=True)
    return path

def next_version(product_id):
    path = os.path.join(DPP_DIR, product_id)
    if not os.path.exists(path):
        return 1
    versions = [
        int(f.replace("v", "").replace(".json", ""))
        for f in os.listdir(path)
        if f.startswith("v")
    ]
    return max(versions) + 1 if versions else 1

def build_dpp(product_id, batch_id, batch_view, compliance_report, factory_id):
    base = ensure_dir(product_id)
    version = next_version(product_id)

    dpp = DPP(
        product_id,
        batch_id,
        version,
        batch_view,
        compliance_report,
        factory_id
    )

    path = os.path.join(base, f"v{version}.json")
    with open(path, "w") as f:
        json.dump(dpp.to_dict(), f, indent=2)

    return path, dpp
