from fastapi import APIRouter

products_router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@products_router.get("/")
async def get_products():
    return {"message": "Get all products"}