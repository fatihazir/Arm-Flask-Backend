import requests

baseUrl = "https://aspnetclusters-101958-0.cloudclusters.net/api"


def SendDataToBackend(results, transactionGroupId, token, isPositive):
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
            "lift": str(result[-1]),
            "isPositive": isPositive
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }

        url = baseUrl + "/Transaction/add"
        res = requests.post(url, json=obj, verify=False, headers=headers)


def CreateTransactionGroupAndForwardToBackend(positiveResults, negativeResults, userId, token, alias):
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
    SendDataToBackend(positiveResults,  res.json()['data']['id'], token, True)
    SendDataToBackend(negativeResults,  res.json()['data']['id'], token, False)
