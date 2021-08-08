from .data import functions

async def GetUsersDetails(name=None,email=None):
    data =  await functions.GetUsersData(name,email)
    return data

async def GetCompanyUserDetails(name=None):
    data = await functions.GetCompanyEmployeeData(name)
    return data