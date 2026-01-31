import os
from dashboard.metrics import dashboard_metrics
from dashboard.pricing import get_plan

def company_dashboard(company_id):
    metrics = dashboard_metrics()
    plan = get_plan("starter")  # later dynamic

    return {
        "company_id": company_id,
        "plan": plan,
        "metrics": metrics
    }
