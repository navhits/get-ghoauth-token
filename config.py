import os

client_id = os.getenv("GH_OAUTH_CLIENT_ID")
client_secret = os.getenv("GH_OAUTH_CLIENT_SECRET")
login = os.getenv("GH_LOGIN")
redirect_uri = "http://localhost:8000/callback"
authorize_endpoint = "https://github.com/login/oauth/authorize"
