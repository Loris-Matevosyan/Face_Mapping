import requests

from .post_access import post_access


def sending_data(serialized_data, token):
    response = post_access(serialized_data, token)

    print(response.status_code)
    print(response.reason)

    return response