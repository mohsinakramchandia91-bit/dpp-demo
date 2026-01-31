from saas.plan import enforce_plan
from saas.billing_guard import enforce_billing

def enforce_all(company_id, plan):
    enforce_billing(company_id)
    enforce_plan(company_id, plan)
    return True
