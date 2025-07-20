from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def process_payment():
    return {"status": "Payment processed successfully"}
