from fastapi import APIRouter
from ..controller import GetUsersDetails
router = APIRouter()



@router.get("/fetch/", tags=["users"])
async def read_users():
    data = await GetUsersDetails()
    print(data)
    return data



