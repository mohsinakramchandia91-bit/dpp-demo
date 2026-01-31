import os

PUBLIC_DIR = "data/public"
AUDIT_DIR = "data/audit_packages"

def count_products():
    if not os.path.exists(PUBLIC_DIR):
        return 0
    return len(os.listdir(PUBLIC_DIR))

def count_audits():
    if not os.path.exists(AUDIT_DIR):
        return 0
    return len(os.listdir(AUDIT_DIR))

def dashboard_metrics():
    return {
        "total_products": count_products(),
        "audit_packages": count_audits()
    }
