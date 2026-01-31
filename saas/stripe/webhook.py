import time

def handle_payment_success(company_id, plan):
    # In real Stripe: this is triggered by webhook

    return {
        "company_id": company_id,
        "plan": plan,
        "status": "paid",
        "activated_at": int(time.time())
    }
