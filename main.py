from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DPP Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "DPP Backend is running"
    }

@app.get("/api/pricing")
def pricing():
    return {
        "plans": [
            {
                "name": "Starter",
                "price": 49,
                "products": 50,
                "factories": 1
            },
            {
                "name": "Business",
                "price": 199,
                "products": 500,
                "factories": 5
            },
            {
                "name": "Enterprise",
                "price": 999,
                "products": "Unlimited",
                "factories": "Unlimited"
            }
        ]
    }

@app.get("/api/analytics/{company_id}")
def analytics(company_id: str):
    return {
        "company_id": company_id,
        "total_events": 12,
        "public_views": 8,
        "verify_checks": 4
    }
