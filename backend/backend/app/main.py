from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Digital Product Passport API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Digital Product Passport API"
    }

@app.get("/api/verify/{product_id}")
def verify(product_id: str):
    return {
        "product_id": product_id,
        "status": "PASS",
        "message": "DPP is valid & untampered"
    }

@app.get("/api/analytics/{company_id}")
def analytics(company_id: str):
    return {
        "company_id": company_id,
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    }
