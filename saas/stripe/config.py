import os

# DO NOT hardcode keys
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "sk_test_placeholder")

PRICE_MAP = {
    "starter": {
        "amount": 49,
        "currency": "usd"
    },
    "business": {
        "amount": 199,
        "currency": "usd"
    },
    "enterprise": {
        "amount": 999,
        "currency": "usd"
    }
}
