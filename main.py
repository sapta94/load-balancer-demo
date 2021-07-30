
from fastapi import FastAPI
from RoundRobin.routers import UserRouter

app = FastAPI()


app.include_router(
    UserRouter.router,
    prefix="/user",
    tags=["users"]
)