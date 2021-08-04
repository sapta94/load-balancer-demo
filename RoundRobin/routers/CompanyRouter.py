import os
import time
from typing import Optional
from fastapi import APIRouter
from ..controller import GetUsersDetails,GetCompanyUserDetails
router = APIRouter()



@router.get("/fetch/empCount", tags=["company"])
async def read_users(name: Optional[str]=None):
    data = await GetCompanyUserDetails(name)
    servername=os.getenv('APP_SERVER')
    resp = {
        "server":servername, 
        "total_company":len(data)
    }
    time.sleep(os.getenv('APP_SLEEP'))
    return resp
