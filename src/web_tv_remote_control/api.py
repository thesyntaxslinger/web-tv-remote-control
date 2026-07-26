import requests
import hmac
from .config import config


def send_key_to_api(key):
    if key not in config.allowed_keys:
        return False
    response = requests.post(
        f'{config.api_url}/key/{key}',
        headers={'Authorization': f'Bearer {config.api_token}'}
    )
    return response.ok

def verify_api_key(auth_header):
    prefix = 'Bearer '
    token = auth_header[len(prefix):] if auth_header.startswith(prefix) else ''
    if not token or not hmac.compare_digest(token, config.api_token):
        return False
    return True
