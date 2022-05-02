import webbrowser
import os
import requests
import uvicorn

from config import *
from app import Server


config = uvicorn.Config("app:app", host="127.0.0.1", port=8000, log_level="error")
server = Server(config=config)


def github_authorize(client_id: str, login: str) -> str:
    url = f"{authorize_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope=user&response_type=code&login={login}"
    code = None
    with server.run_in_thread():
        
        print("If browser window does not open automatically, open it by clicking on the link:")
        print(f"{url}\n\n")
        webbrowser.open_new_tab(url)
        
        while not code:
            import shelve
            with shelve.open('oauth', 'c') as db:
                code = db.get('code')
                if code:
                    db.clear()
                    os.remove('oauth')
        return code
    
def get_oauth_token(client_id: str, client_secret: str, login: str) -> str:
    code = github_authorize(client_id=client_id, login=login)
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
        print(f"Token is valid. User login: {user}")
    else:
        print("Token is invalid")
