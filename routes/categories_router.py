from fastapi import APIRouter

categories_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@categories_router.get("/")
async def get_categories():
    return {"message": "Get all categories"}