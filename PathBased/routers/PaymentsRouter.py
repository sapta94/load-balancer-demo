import os
from typing import Optional
from fastapi import APIRouter
from ..controller import GetUserPaymentsData
router = APIRouter()



@router.get("/fetch/paymentData", tags=["payments"])
async def read_users(email: Optional[str]=None):
    data = await GetUserPaymentsData(email)
    servername=os.getenv('APP_SERVER')
    resp = {
        "server":servername, 
        "payments":data
    }
    
    return resp
