from saas.stripe.checkout import create_checkout_session
from saas.stripe.webhook import handle_payment_success

def start_payment(company_id, plan):
    session = create_checkout_session(company_id, plan)
    return session

def confirm_payment(company_id, plan):
    return handle_payment_success(company_id, plan)
