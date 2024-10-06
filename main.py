from fastapi import FastAPI
from routes import admin_router, carts_router, categories_router, payments_router, products_router, auth_router, orders_router, users_router
from database.db import engine, Base

#this line tells sqlalchemy to run the create statement to generate all of the tables in the beginning
#This line won't be needed if we are going to use Alembic for tables creation and architecture changes over time.
print(Base)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin_router)
app.include_router(carts_router)
app.include_router(categories_router)
app.include_router(payments_router)
app.include_router(products_router)
app.include_router(users_router)
app.include_router(orders_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}