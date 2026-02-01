from flask import request, jsonify
from db.database import get_db

def require_api_key():
    key = request.headers.get("X-API-KEY")
    if not key:
        return False

    db = get_db()
    company = db.execute(
        "SELECT * FROM companies WHERE api_key = ?",
        (key,)
    ).fetchone()
    db.close()

    return company
