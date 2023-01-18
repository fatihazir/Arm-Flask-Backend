import requests

baseUrl = "https://localhost:5201/api"


def SendDataToBackend(results, transactionGroupId, token):
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

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }

        url = baseUrl + "/Transaction/add"
        res = requests.post(url, json=obj, verify=False, headers=headers)


def CreateTransactionGroupAndForwardToBackend(results, userId, token, alias):
    obj = {
        "userId": userId,
        "alias": alias
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    url = baseUrl + "/UserTransactionGroup/add"

    res = requests.post(url, json=obj, verify=False, headers=headers)
    SendDataToBackend(results,  res.json()['data']['id'], token)
