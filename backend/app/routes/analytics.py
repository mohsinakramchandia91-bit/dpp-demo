from fastapi import APIRouter

router = APIRouter()

@router.get("/{company_id}")
def analytics(company_id: str):
    return {
        "company_id": company_id,
        "public_views": 8,
        "verify_checks": 4
    }
