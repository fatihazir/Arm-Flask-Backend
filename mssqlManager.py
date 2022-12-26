def SaveToDatabase(results, transactionGroupId):
    for result in results:
        associations = result[0:-3]
        tempSupport = result[-3]
        tempConfidence = result[-2]
        tempLift = result[-1]

        InsertIntoDatabase(transactionGroupId, associations,
                           tempSupport, tempConfidence, tempLift)


def InsertIntoDatabase(transactionGroupId, associations, tempSupport, tempConfidence, tempLift):
    print(associations)
    print(tempSupport)
    print(tempConfidence)
    print(tempLift)
    print('---------------')
    # .nete istek atıp veriyi ekle. sonrasında işlem tamam, transaction group id vs veririsn. result olarak da bunu da dön.


def CreateTransactionGroup(userId):
    # .nete istek atıp oluşturulan transaction group idsini dön.
    return 100
