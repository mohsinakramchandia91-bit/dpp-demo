from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Digital Product Passport API"
    }

@app.get("/api/analytics/{company_id}")
def analytics(company_id: str):
    return {
        "company_id": company_id,
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    }
