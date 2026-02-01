from flask import Flask, jsonify, request
from flask_cors import CORS
from db.database import get_db
from auth.auth import require_api_key

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "ok", "service": "DPP SaaS API"}

@app.route("/api/analytics")
def analytics():
    company = require_api_key()
    if not company:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "company_id": company["id"],
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    })

@app.route("/api/verify/<product_id>")
def verify(product_id):
    return jsonify({
        "product_id": product_id,
        "status": "PASS",
        "message": "Verified Digital Product Passport"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
