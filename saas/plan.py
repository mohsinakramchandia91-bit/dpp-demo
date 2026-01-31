from dashboard.pricing import get_plan
from dashboard.metrics import dashboard_metrics

class PlanLimitError(Exception):
    pass

def enforce_plan(company_id, plan_name):
    plan = get_plan(plan_name)
    if not plan:
        raise PlanLimitError("Invalid plan")

    metrics = dashboard_metrics()

    # product limit
    if plan["products"] != "unlimited":
        if metrics["total_products"] >= plan["products"]:
            raise PlanLimitError("Product limit exceeded")

    # audit limit (simple rule: audits = products)
    if plan["products"] != "unlimited":
        if metrics["audit_packages"] >= plan["products"]:
            raise PlanLimitError("Audit limit exceeded")

    return True
