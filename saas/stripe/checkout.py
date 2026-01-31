import time
from saas.stripe.config import PRICE_MAP

def create_checkout_session(company_id, plan):
    if plan not in PRICE_MAP:
        raise ValueError("Invalid plan")

    price = PRICE_MAP[plan]

    # Stripe API call will go here later
    # For now we simulate a real checkout session
    session = {
        "session_id": f"cs_{int(time.time())}",
        "company_id": company_id,
        "plan": plan,
        "amount": price["amount"],
        "currency": price["currency"],
        "payment_url": f"https://checkout.stripe.com/pay/cs_test_{company_id}",
        "status": "created"
    }

    return session
