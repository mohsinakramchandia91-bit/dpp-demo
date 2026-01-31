import os
from saas.billing import billing_status

BASE_DIR = "data"

def with_company(company_id):
    company_dir = os.path.join(BASE_DIR, company_id)
    os.makedirs(company_dir, exist_ok=True)

    plan_file = os.path.join(company_dir, "plan.txt")
    if not os.path.exists(plan_file):
        with open(plan_file, "w") as f:
            f.write("starter")

    with open(plan_file) as f:
        plan = f.read().strip()

    paths = {
        "PUBLIC_DIR": os.path.join(company_dir, "public"),
        "PROOF_DIR": os.path.join(company_dir, "proof"),
        "AUDIT_DIR": os.path.join(company_dir, "audit_packages"),
        "QR_DIR": os.path.join(company_dir, "qr"),
        "DPP_DIR": os.path.join(company_dir, "dpp"),
        "PLAN": plan,
        "BILLING_STATUS": billing_status(company_id)
    }

    for k, v in paths.items():
        if k.endswith("_DIR"):
            os.makedirs(v, exist_ok=True)

    return paths
