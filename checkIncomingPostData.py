def CheckIncomingPostDataIsValid(data, minSupport, maxLength, minLength, elementAmount):
    if ((type(data) == list) and (type(data[0] == list)) and (type(minSupport) == float) and
            (type(maxLength) == int) and (type(minLength) == int) and (type(elementAmount) == int)):
        return True
    else:
        return False
