import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--validate", help="Use this flag to validate the recieved token", action="store_true")
if __name__ == '__main__':
    from github import get_oauth_token, validate_token
    from config import *
    args = parser.parse_args()
    token = get_oauth_token(client_id, client_secret, login)
    print(f"Oauth Token: {token} \n")
    if args.validate:
        validate_token(token)
