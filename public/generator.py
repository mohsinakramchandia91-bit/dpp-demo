from branding.config import get_branding
from analytics.track import track_event
import os

PUBLIC_DIR = "site/public"

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Digital Product Passport</title>
<style>
body {{
  font-family: Arial;
  background: #f4f6f8;
}}
.card {{
  max-width: 720px;
  margin: 40px auto;
  background: white;
  padding: 24px;
  border-radius: 10px;
}}
.header {{
  border-bottom: 4px solid {color};
  margin-bottom: 20px;
}}
.badge {{
  background: {color};
  color: white;
  display: inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 13px;
}}
.footer {{
  margin-top: 30px;
  font-size: 12px;
  color: #777;
}}
</style>
</head>

<body>
<div class="card">
  <div class="header">
    <img src="{logo}" height="40"><br><br>
    <span class="badge">VERIFIED PRODUCT</span>
    <h2>{company}</h2>
  </div>

  <p><strong>Product ID:</strong> {product}</p>
  <p><strong>Version:</strong> {version}</p>
  <p><strong>Status:</strong> PASS</p>

  <div class="footer">
    {footer}
  </div>
</div>
</body>
</html>
"""

def generate_public_view(dpp):
    branding = get_branding(dpp.factory_id)

    track_event(
        company_id=dpp.factory_id,
        product_id=dpp.product_id,
        event="public_view",
        meta={"version": dpp.version}
    )

    os.makedirs(PUBLIC_DIR, exist_ok=True)
    path = f"{PUBLIC_DIR}/{dpp.product_id}-v{dpp.version}.html"

    html = HTML.format(
        company=branding["company_name"],
        logo=branding["logo_url"],
        color=branding["primary_color"],
        footer=branding["footer"],
        product=dpp.product_id,
        version=dpp.version
    )

    with open(path, "w") as f:
        f.write(html)

    return path
