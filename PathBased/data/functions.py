from . import dataset

async def GetUsersData(name=None, email=None):
    results = []
    userData = dataset.GenerateDataset()
    for item in userData:
        if name and email and (item['first_name']==name or item['last_name']==name) and item['email']==email:
            results.append(item)
        elif name and (item['first_name']==name or item['last_name']==name):
            results.append(item)
        elif email and item['email']==email:
            results.append(item)
        elif not name and  not email:
            results.append(item)

    return results[0:50]

async def GetCompanyEmployeeData(name=None):
    results = {}
    companyData = dataset.GenerateDataset()

    for item in companyData:
        if item['company'] in results:
            results[item['company']]+=1
        else:
            results[item['company']]=1

    if name:
        return results.get(name)
    else:
        return results

async def GetPaymentsData(email=None):
    results = []
    paymentsData = dataset.GeneratePaymentsData()

    for item in paymentsData:
        if email and item['email']==email:
            results.append(item)
        elif not email:
            results.append(item)

    return results
    
        
            