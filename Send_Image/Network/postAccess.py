import requests

from .url import getBaseURL


def postAccess(payload, token):

    protected_url = f'{getBaseURL()}/image'
    headers = { "Authorization" : f'Bearer {token}',
                "Content-Type" : "application/json"}
    response = requests.post(protected_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Data has been received")
    else:
        print("Failed to send the data to the protected URL: ", response.json().get("message"))

    return response