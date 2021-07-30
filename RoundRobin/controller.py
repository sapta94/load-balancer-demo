from .data import functions

async def GetUsersDetails(name=None,email=None):
    data =  functions.GetUsersData(name,email)
    return data