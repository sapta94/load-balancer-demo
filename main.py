
from fastapi import FastAPI
from RoundRobin.routers import UserRouter, CompanyRouter

app = FastAPI()

app.include_router(
    UserRouter.router,
    prefix="/user",
    tags=["users"]
)

app.include_router(
    CompanyRouter.router,
    prefix="/company",
    tags=["company"]
)