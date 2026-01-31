import os
import time
import json

BILLING_DIR = "data/billing"

PLANS = {
    "starter": 49,
    "business": 199,
    "enterprise": 999
}

def ensure_company_billing(company_id):
    path = os.path.join(BILLING_DIR, company_id)
    os.makedirs(path, exist_ok=True)
    return path

def charge_company(company_id, plan):
    ensure_company_billing(company_id)

    amount = PLANS.get(plan)
    if not amount:
        raise Exception("Invalid plan")

    invoice = {
        "company_id": company_id,
        "plan": plan,
        "amount_usd": amount,
        "currency": "USD",
        "status": "paid",
        "timestamp": int(time.time())
    }

    invoice_path = os.path.join(
        BILLING_DIR,
        company_id,
        f"invoice_{invoice['timestamp']}.json"
    )

    with open(invoice_path, "w") as f:
        json.dump(invoice, f, indent=2)

    return invoice

def billing_status(company_id):
    path = os.path.join(BILLING_DIR, company_id)
    if not os.path.exists(path):
        return "inactive"

    invoices = os.listdir(path)
    return "active" if invoices else "inactive"
