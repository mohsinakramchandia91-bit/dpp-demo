from fastapi import FastAPI
from app.routes.verify import router as verify_router
from app.routes.analytics import router as analytics_router

app = FastAPI(title="DPP SaaS API")

app.include_router(verify_router, prefix="/verify")
app.include_router(analytics_router, prefix="/analytics")

@app.get("/")
def root():
    return {"status": "DPP API live"}
