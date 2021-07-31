from typing import Optional
from fastapi import APIRouter
from ..controller import GetUsersDetails,GetCompanyUserDetails
router = APIRouter()



@router.get("/fetch/empCount", tags=["company"])
async def read_users(name: Optional[str]=None):
    data = await GetCompanyUserDetails(name)
    #print(data)
    return data