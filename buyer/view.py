import os
from auditor.verifier import verify_dpp
from saas.branding import get_branding
from buyer.domain_resolver import get_verify_path

HTML = """
<html>
<head>
<title>{company_name} – Verification</title>
<style>
body {{ font-family: Arial; background:#f1f5f9; }}
.card {{ max-width:700px; margin:40px auto; background:white; padding:24px; border-radius:10px; }}
.status {{ font-size:22px; font-weight:bold; color:{color}; }}
</style>
</head>
<body>
<div class="card">
<h2>{company_name}</h2>
<p>Product ID: <strong>{product_id}</strong></p>
<p>Version: <strong>{version}</strong></p>
<p class="status">{status}</p>
<p>{message}</p>
<p style="font-size:12px;color:#666;">Independent verification supported</p>
</div>
</body>
</html>
"""

def generate_verify_page(company_id, product_id, version):
    valid, message = verify_dpp(product_id, version)
    branding = get_branding(company_id)

    html = HTML.format(
        company_name=branding["company_name"],
        product_id=product_id,
        version=version,
        status="PASS" if valid else "FAIL",
        message=message,
        color=branding["theme_color"]
    )

    path = get_verify_path(company_id, product_id, version)

    with open(path, "w") as f:
        f.write(html)

    return path
