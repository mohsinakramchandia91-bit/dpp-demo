import os
from analytics.track import track_event

PUBLIC_DIR = "data/public"

HTML_TEMPLATE = """
<html>
<head>
<title>Digital Product Passport</title>
<style>
body {{
  font-family: Arial;
  background: #f4f6f8;
}}
.card {{
  max-width: 800px;
  margin: auto;
  background: white;
  padding: 20px;
  border-radius: 8px;
}}
.status-pass {{ color: green; font-weight: bold; }}
.status-fail {{ color: red; font-weight: bold; }}
</style>
</head>
<body>
<div class="card">
<h2>Digital Product Passport</h2>

<p><strong>Product ID:</strong> {product_id}</p>
<p><strong>Batch ID:</strong> {batch_id}</p>
<p><strong>Version:</strong> {version}</p>
<p><strong>Status:</strong>
<span class="status-{status_lower}">{status}</span>
</p>

<hr>

<h3>Material</h3>
<p>{material}</p>

<h3>Composition</h3>
<p>{cotton_percent}% Cotton</p>

<h3>Sustainability</h3>
<p>Energy Source: {energy_source}</p>
<p>Confidence: {confidence}%</p>

<hr>

<h3>Public Verification</h3>
<pre>{public_path}</pre>

<p style="font-size:12px;color:#666">
Self-declared manufacturer data.<br>
Cryptographically verifiable.<br>
Independent audit supported.
</p>

</div>
</body>
</html>
"""

def generate_public_view(dpp):
    product_dir = os.path.join(PUBLIC_DIR, dpp.product_id)
    os.makedirs(product_dir, exist_ok=True)

    path = os.path.join(product_dir, f"v{dpp.version}.html")

    # 🔥 ANALYTICS TRACKING (PUBLIC PAGE HIT)
    track_event(
        company_id=dpp.factory_id,
        product_id=dpp.product_id,
        event="public_view",
        meta={"version": dpp.version}
    )

    html = HTML_TEMPLATE.format(
        product_id=dpp.product_id,
        batch_id=dpp.batch_id,
        version=dpp.version,
        status=dpp.compliance_report.get("status"),
        status_lower=dpp.compliance_report.get("status").lower(),
        material=dpp.batch_view.get("material", {}).get("value", "N/A"),
        cotton_percent=dpp.batch_view.get("cotton_percent", {}).get("value", 0),
        energy_source=dpp.batch_view.get("energy_source", {}).get("value", "N/A"),
        confidence=dpp.batch_view.get("material", {}).get("confidence", 0),
        public_path=path
    )

    with open(path, "w") as f:
        f.write(html)

    return path
