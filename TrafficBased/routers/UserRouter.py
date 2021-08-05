import os
import time
from typing import Optional
from fastapi import APIRouter
from ..controller import GetUsersDetails
router = APIRouter()



@router.get("/fetch/", tags=["users"])
async def read_users(name: Optional[str]=None, email: Optional[str]=None):
    data = await GetUsersDetails(name,email )
    #print(data)
    servername=os.getenv('APP_SERVER')
    resp = {
        "server":servername, 
        "total_users":len(data)
    }
    #print(type(os.getenv('APP_SLEEP')))
    time.sleep(int(os.getenv('APP_SLEEP')))
    return resp



