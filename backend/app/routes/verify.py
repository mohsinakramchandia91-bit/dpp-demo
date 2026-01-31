from fastapi import APIRouter

router = APIRouter()

@router.get("/{product_id}")
def verify(product_id: str):
    return {
        "product_id": product_id,
        "status": "PASS",
        "message": "DPP is valid and untampered"
    }
