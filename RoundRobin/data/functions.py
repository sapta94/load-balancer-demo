from . import dataset

async def GetUsersData(name=None, email=None):
    results = []
    userData = dataset.GenerateDataset()
    for item in userData:
        if name and email and item['name']==name and item['email']==email:
            results.append(item)
        elif name and item['name']==name:
            results.append(item)
        elif email and item['email']==email:
            results.append(item)
        else:
            results.append(item)

