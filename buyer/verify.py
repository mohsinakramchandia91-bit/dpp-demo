import os
from analytics.track import track_event
from proof.verifier import verify_dpp

PUBLIC_VERIFY_DIR = "data/verify"

HTML = """
<html>
<head>
<title>Buyer Verification</title>
<style>
body {{ font-family: Arial; background:#f4f6f8; }}
.card {{ max-width:600px; margin:auto; background:white; padding:20px; }}
.pass {{ color:green; font-weight:bold; }}
.fail {{ color:red; font-weight:bold; }}
</style>
</head>
<body>
<div class="card">
<h2>Verification Result</h2>
<p><strong>Product ID:</strong> {product_id}</p>
<p><strong>Version:</strong> {version}</p>
<p class="{status_class}">{status}</p>
<p>{message}</p>
</div>
</body>
</html>
"""

def generate_verify_page(product_id, version, company_id):
    os.makedirs(PUBLIC_VERIFY_DIR, exist_ok=True)

    valid, message = verify_dpp(product_id, version)

    # 🔥 ANALYTICS TRACKING (VERIFY HIT)
    track_event(
        company_id=company_id,
        product_id=product_id,
        event="verify_check",
        meta={"version": version}
    )

    html = HTML.format(
        product_id=product_id,
        version=version,
        status="PASS" if valid else "FAIL",
        status_class="pass" if valid else "fail",
        message=message
    )

    path = os.path.join(PUBLIC_VERIFY_DIR, f"{product_id}-v{version}.html")
    with open(path, "w") as f:
        f.write(html)

    return path
