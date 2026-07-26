import hmac
import urllib.parse
import urllib.request
import urllib.error

from .config import config


def make_request(key):
    data = urllib.parse.quote(key)
    headers = {'Authorization': f'Bearer {config.api_token}'}
    req = urllib.request.Request(f'{config.api_url}/key/{data}', headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req):
            pass
    except urllib.error.HTTPError as e:
        print(f'ERROR: API request failed with code {e.code}')
        return False
    except urllib.error.URLError as e:
        print(f'ERROR: API request failed {e.reason}')
        return False
    else:
        return True


def send_key_to_api(key):
    if key not in config.allowed_keys:
        return False
    status = make_request(key)
    return status


def verify_api_key(auth_header):
    if not auth_header:
        return False
    prefix = 'Bearer '
    token = auth_header[len(prefix):] if auth_header.startswith(prefix) else ''
    if not token or not hmac.compare_digest(token, config.api_token):
        return False
    return True
