from branding.config import get_branding
from analytics.track import track_event
import os

VERIFY_DIR = "site/verify"

HTML = """
<html>
<head>
<title>Verification Result</title>
<style>
body {{
  font-family: Arial;
  background: #f4f6f8;
}}
.card {{
  max-width: 520px;
  margin: 60px auto;
  background: white;
  padding: 24px;
  border-radius: 10px;
  text-align: center;
}}
.pass {{
  color: green;
  font-weight: bold;
}}
</style>
</head>

<body>
<div class="card">
  <img src="{logo}" height="40"><br><br>
  <h2>{company}</h2>

  <p>Product ID: <strong>{product}</strong></p>
  <p>Version: {version}</p>
  <p class="pass">PASS</p>

  <small>{footer}</small>
</div>
</body>
</html>
"""

def generate_verify_page(product_id, version, company_id):
    branding = get_branding(company_id)

    track_event(
        company_id=company_id,
        product_id=product_id,
        event="verify_check",
        meta={"version": version}
    )

    os.makedirs(VERIFY_DIR, exist_ok=True)
    path = f"{VERIFY_DIR}/{product_id}-v{version}.html"

    html = HTML.format(
        company=branding["company_name"],
        logo=branding["logo_url"],
        footer=branding["footer"],
        product=product_id,
        version=version
    )

    with open(path, "w") as f:
        f.write(html)

    return path
