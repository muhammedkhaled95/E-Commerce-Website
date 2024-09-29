from fastapi import APIRouter

carts_router = APIRouter(
    prefix="/carts",
    tags=["Carts"]
)

@carts_router.get("/")
async def get_carts():
    return {"message": "Get all carts"}

