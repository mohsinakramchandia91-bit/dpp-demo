from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DPP Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "DPP backend running"}

@app.get("/analytics/{company_id}")
def analytics(company_id: str):
    return {
        "company_id": company_id,
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    }
