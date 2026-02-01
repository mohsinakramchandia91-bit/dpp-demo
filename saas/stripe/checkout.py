import stripe
from saas.stripe.config import PRICE_MAP

stripe.api_key = "sk_test_YOUR_KEY"

def create_checkout(company_id, plan):
    price = PRICE_MAP[plan]["price_id"]

    session = stripe.checkout.Session.create(
        mode="subscription",
        payment_method_types=["card"],
        line_items=[{"price": price, "quantity": 1}],
        success_url=f"https://YOURDOMAIN/success.html?c={company_id}",
        cancel_url=f"https://YOURDOMAIN/cancel.html"
    )

    return session.url
