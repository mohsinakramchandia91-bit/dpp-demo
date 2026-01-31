import os

DASHBOARD_DIR = "data/dashboard"

HTML = """
<html>
<head>
<title>Company Dashboard</title>
<style>
body {{ font-family: Arial; background:#f4f6f8; }}
.card {{ max-width:800px; margin:auto; background:white; padding:20px; border-radius:8px; }}
.stat {{ font-size:22px; margin:10px 0; }}
</style>
</head>
<body>
<div class="card">
<h2>Company Dashboard</h2>

<p><strong>Plan:</strong> {plan}</p>

<hr>

<div class="stat">📦 Products Created: {products}</div>
<div class="stat">🗂 Audit Packages: {audits}</div>

<hr>
<p>All data is cryptographically protected.</p>
</div>
</body>
</html>
"""

def generate_dashboard(company_id, data):
    os.makedirs(DASHBOARD_DIR, exist_ok=True)

    html = HTML.format(
        plan=data["plan"]["price_monthly"],
        products=data["metrics"]["total_products"],
        audits=data["metrics"]["audit_packages"]
    )

    path = os.path.join(DASHBOARD_DIR, f"{company_id}.html")
    with open(path, "w") as f:
        f.write(html)

    return path
