from fastapi import FastAPI

from app.products.routers import router as router_products
from app.auth.routers import router as router_auth

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_products)
