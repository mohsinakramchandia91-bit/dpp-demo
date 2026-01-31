import os
from dashboard.charts import analytics_summary

DASHBOARD_DIR = "data/dashboard_analytics"

HTML = """
<html>
<head>
<title>Analytics Dashboard</title>
<style>
body {{ font-family: Arial; background:#f4f6f8; }}
.card {{ max-width:900px; margin:20px auto; background:white; padding:20px; border-radius:8px; }}
h2 {{ margin-top:0; }}
.bar {{ background:#4caf50; height:18px; margin:6px 0; }}
.small {{ color:#666; font-size:13px; }}
</style>
</head>
<body>

<div class="card">
<h2>📊 Company Analytics</h2>

<p><strong>Total Events:</strong> {total_events}</p>

<h3>Events</h3>
{event_rows}

<h3>Top Products</h3>
{product_rows}

<h3>Daily Activity</h3>
{day_rows}

<p class="small">
Tracked automatically via QR & buyer verification.<br>
Data is immutable & auditable.
</p>
</div>

</body>
</html>
"""

def _bars(data):
    rows = ""
    max_val = max(data.values()) if data else 1
    for k, v in data.items():
        width = int((v / max_val) * 100)
        rows += f"<div>{k} ({v})<div class='bar' style='width:{width}%'></div></div>"
    return rows

def generate_analytics_dashboard(company_id):
    os.makedirs(DASHBOARD_DIR, exist_ok=True)

    s = analytics_summary(company_id)

    html = HTML.format(
        total_events=s["total_events"],
        event_rows=_bars(s["by_event"]),
        product_rows=_bars(s["by_product"]),
        day_rows=_bars(s["by_day"])
    )

    path = os.path.join(DASHBOARD_DIR, f"{company_id}.html")
    with open(path, "w") as f:
        f.write(html)

    return path
