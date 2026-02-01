from dashboard.analytics import company_analytics

def company_dashboard(company_id):
  return {
    "analytics": company_analytics(company_id),
    "billing": "active",
    "plan": "starter"
  }
