import secrets

def make_api_token():
    token = secrets.token_urlsafe(32)
    return token
