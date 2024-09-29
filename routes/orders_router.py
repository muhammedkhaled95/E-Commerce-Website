from fastapi import APIRouter

orders_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@orders_router.get("/")
async def read_orders():
    return [{"item_id": "Foo"}]
