import os
from saas.domain import get_domain

BASE_PUBLIC_DIR = "data/public_domains"

def get_verify_path(company_id, product_id, version):
    domain = get_domain(company_id)

    if not domain:
        # fallback to default
        return os.path.join("data/verify", f"{product_id}-v{version}.html")

    domain_dir = os.path.join(BASE_PUBLIC_DIR, domain)
    os.makedirs(domain_dir, exist_ok=True)

    return os.path.join(domain_dir, f"{product_id}-v{version}.html")
