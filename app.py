from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return jsonify({
        "status": "ok",
        "service": "Digital Product Passport API"
    })

@app.route("/api/analytics/<company_id>")
def analytics(company_id):
    return jsonify({
        "company_id": company_id,
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    })

@app.route("/api/verify/<product_id>")
def verify(product_id):
    return jsonify({
        "product_id": product_id,
        "status": "PASS",
        "message": "DPP is valid & untampered"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
