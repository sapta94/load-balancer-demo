
from fastapi import FastAPI
from PathBased.routers import UserRouter, CompanyRouter, PaymentsRouter

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

app.include_router(
    PaymentsRouter.router,
    prefix="/payments",
    tags=["payments"]
)