import webbrowser
import time

import requests
import uvicorn

from config import *
from app import Server


config = uvicorn.Config("app:app", host="127.0.0.1", port=8000, log_level="error")
server = Server(config=config)


def github_authorize(client_id: str, login: str, nobrowser: bool) -> str:
    url = f"{authorize_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope=user&response_type=code&login={login}"
    with server.run_in_thread():
        if nobrowser:
            print("Visit this URL to complete the Oauth flow")
            print(f"{url}\n\n")
        else:    
            webbrowser.open_new_tab(url)
        time.sleep(10)
    
    import dbm
    with dbm.open('oauth', 'c') as db:
        code = db['code']
        del db['code']
    return code.decode('utf-8')
    
def get_oauth_token(client_id: str, client_secret: str, login: str, nobrowser: bool) -> str:
    code = github_authorize(client_id=client_id, login=login, nobrowser=nobrowser)
    res = requests.post("https://github.com/login/oauth/access_token", data={"client_id": client_id, "client_secret": client_secret, "code": code, "redirect_uri": redirect_uri})
    return res.text.split("&")[0].split("=")[1]


def validate_token(token: str) -> None:
    api_endpoint = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}"
    }
    res = requests.get(api_endpoint, headers=headers)
    user = res.json().get('login')
    if user:
        if user == login:
            print("Token is valid")
    else:
        print("Token is invalid")

