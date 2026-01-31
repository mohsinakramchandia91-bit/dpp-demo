import os
from datetime import datetime

BASE_DIR = "data/public"

def ensure_dir(product_id):
    path = os.path.join(BASE_DIR, product_id)
    os.makedirs(path, exist_ok=True)
    return path

def generate_public_view(dpp_obj):
    product_path = ensure_dir(dpp_obj.product_id)
    file_name = f"v{dpp_obj.version}.html"
    file_path = os.path.join(product_path, file_name)

    html = []
    html.append("<html>")
    html.append("<head><title>Digital Product Passport</title></head>")
    html.append("<body>")
    html.append("<h1>Digital Product Passport</h1>")

    html.append("<h2>Product Info</h2>")
    html.append(f"<p><b>Product ID:</b> {dpp_obj.product_id}</p>")
    html.append(f"<p><b>Batch ID:</b> {dpp_obj.batch_id}</p>")
    html.append(f"<p><b>DPP Version:</b> {dpp_obj.version}</p>")
    html.append(f"<p><b>Created At:</b> {dpp_obj.created_at}</p>")

    html.append("<h2>Compliance Status</h2>")
    html.append(f"<p><b>Status:</b> {dpp_obj.compliance_report['status']}</p>")
    html.append(f"<p><b>Batch Confidence:</b> {dpp_obj.compliance_report['batch_confidence']}</p>")

    html.append("<h3>Risks</h3>")
    if dpp_obj.compliance_report["risks"]:
        html.append("<ul>")
        for r in dpp_obj.compliance_report["risks"]:
            html.append(f"<li>{r}</li>")
        html.append("</ul>")
    else:
        html.append("<p>No risks identified</p>")

    html.append("<h2>Material & Sustainability Data</h2>")
    html.append("<table border='1' cellpadding='5'>")
    html.append("<tr><th>Field</th><th>Value</th><th>Confidence</th></tr>")

    for field, data in dpp_obj.batch_view.items():
        html.append(
            f"<tr><td>{field}</td>"
            f"<td>{data.get('value')}</td>"
            f"<td>{data.get('confidence')}</td></tr>"
        )

    html.append("</table>")

    html.append("<hr>")
    html.append("<p>This Digital Product Passport is system-generated and read-only.</p>")
    html.append("</body></html>")

    with open(file_path, "w") as f:
        f.write("\n".join(html))

    return file_path
