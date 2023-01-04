import requests


def SendDataToBackend(results, transactionGroupId):
    for result in results:

        tempAssociationsString = ""

        for i in range(len(result[0:-3])):
            try:
                tempAssociationsString += result[0:-3][i]

                if ((i+1) != len(result[0:-3])):
                    tempAssociationsString += ","
            except:
                pass

        obj = {
            "transactionGroupId": transactionGroupId,
            "associations": tempAssociationsString,
            "support": str(result[-3]),
            "confidence": str(result[-2]),
            "lift": str(result[-1])
        }

        url = "http://localhost:5200/api/Transaction/add"
        res = requests.post(url, json=obj, verify=False)


def CreateTransactionGroupAndForwardToBackend(results, userId, alias):
    obj = {
        "userId": userId,
        "alias": alias
    }
    url = "http://localhost:5200/api/UserTransactionGroup/add"

    res = requests.post(url, json=obj, verify=False)
    SendDataToBackend(results,  res.json()['data']['id'])
