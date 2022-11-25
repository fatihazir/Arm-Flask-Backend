def SuccessResult(data, message):
    return {
        'Success': True,
        'Message': message,
        'Data ': data
    }

def ErrorResult(message):
    return {
        'Success': False,
        'Message': message,
        'Data ': {}
    }


