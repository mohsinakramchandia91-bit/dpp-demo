PRICING_PLANS = {
    "starter": {
        "price_monthly": 49,
        "products": 50,
        "factories": 1,
        "support": "email"
    },
    "business": {
        "price_monthly": 199,
        "products": 500,
        "factories": 5,
        "support": "priority"
    },
    "enterprise": {
        "price_monthly": 999,
        "products": "unlimited",
        "factories": "unlimited",
        "support": "dedicated"
    }
}

def get_plan(plan_name):
    return PRICING_PLANS.get(plan_name, None)
