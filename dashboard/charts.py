from collections import Counter, defaultdict
from dashboard.analytics import company_analytics
import datetime

def analytics_summary(company_id):
    events = company_analytics(company_id)

    summary = {
        "total_events": len(events),
        "by_event": Counter(),
        "by_product": Counter(),
        "by_day": defaultdict(int)
    }

    for e in events:
        summary["by_event"][e["event"]] += 1
        summary["by_product"][e["product_id"]] += 1

        day = datetime.datetime.fromtimestamp(
            e["timestamp"]
        ).strftime("%Y-%m-%d")
        summary["by_day"][day] += 1

    return summary
