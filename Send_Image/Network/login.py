import requests

from .url import getBaseURL


def login(username, password):

    login_url = f'{getBaseURL()}/login'
    payload = {"username": username, "password" : password}
    response = requests.post(login_url, json=payload)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        print("Login successfully")
        return access_token
    else:
        print(f"Failed to login: ", response.json().get("message"))
        return None
