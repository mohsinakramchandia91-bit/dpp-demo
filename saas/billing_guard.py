from saas.billing import billing_status

class BillingError(Exception):
    pass

def enforce_billing(company_id):
    status = billing_status(company_id)
    if status != "active":
        raise BillingError("Billing inactive – payment required")
    return True
