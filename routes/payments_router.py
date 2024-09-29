from fastapi import APIRouter

payments_router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@payments_router.post("/")
async def create_payment():
    return {"message": "Payment created successfully"}
