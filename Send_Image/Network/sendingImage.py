import requests

from .postAccess import postAccess


def sendingData(serialized_data, token):
    response = postAccess(serialized_data, token)

    print(response.status_code)
    print(response.reason)

    return response


