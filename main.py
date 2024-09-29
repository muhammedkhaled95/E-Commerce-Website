from fastapi import FastAPI
from routes import admin_router, carts_router, categories_router, payments_router, products_router, users_router, orders_router


app = FastAPI()

app.include_router(admin_router)
app.include_router(carts_router)
app.include_router(categories_router)
app.include_router(payments_router)
app.include_router(products_router)
app.include_router(users_router)
app.include_router(orders_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}