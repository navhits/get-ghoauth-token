# Get Oauth token from Github API for your Oauth application

This small script gets you the Oauth token for your Github Oauth application.

Note: When you create the Oauth application, the `Authorization callback URL` should be set to `http://localhost:8000/oauth/callback` in order for this script to work. This can be also be edited in the Github Oauth application settings at <https://github.com/settings/applications/:applicationId:>

You need to provide the following environment variables:

1. `GH_OAUTH_CLIENT_ID` - The client ID of your Oauth application
2. `GH_OAUTH_CLIENT_SECRET` - Generate a client secret in your Oauth application and add it here
3. `GH_LOGIN` - The users Github login ID

Here are the steps to run this script

```bash
git clone https://github.com/navhits/get-ghoauth-token.git
cd get-ghoauth-token
python3 -m virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 get_gho.py --nobrowser --validate
```

Want docker?

```bash
export GH_OAUTH_CLIENT_ID=<your client id>
export GH_OAUTH_CLIENT_SECRET=<your client secret>
export GH_LOGIN=<your github login>
env | grep GH_ > .env
docker pull ghcr.io/navhits/get-ghoauth-token/get-gho:latest
docker tag ghcr.io/navhits/get-ghoauth-token/get-gho:latest get-gho:latest
docker run --rm --env-file .env get-ghoauth-token:latest --validate
```

The flags `--nobrowser` and `--validate` are optional. (`--nobrowser` is set by default in the docker image)

* `--nobrowser` will tell the script to present the authorization URL in terminal and not open the browser. This is useful for non-interactive environments.
* `--validate` will tell the script to validate the recieved Oauth token.
