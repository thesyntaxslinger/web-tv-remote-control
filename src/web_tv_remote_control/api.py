import hmac
import urllib.parse
import urllib.request
import urllib.error
from wakeonlan import send_magic_packet

from .ssh import ssh_api_and_turn_off
from .config import config


def make_request(key):
    data = urllib.parse.quote(key)
    headers = {'Authorization': f'Bearer {config.api_token}'}
    req = urllib.request.Request(f'{config.api_url}/key/{data}', headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=5):
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
    if key in config.allowed_keys:
        make_request(key)
        return True

    if key in config.special_keys:
        if key == 'on' and config.mode == 'controller':
            send_magic_packet(config.api_macaddress)
            return True
        if key == 'off' and config.mode == 'controller':
            # command="/sbin/poweroff",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 AAA...
            ssh_api_and_turn_off()
            return True
    return False


def verify_api_key(auth_header):
    if not auth_header:
        return False
    prefix = 'Bearer '
    token = auth_header[len(prefix):] if auth_header.startswith(prefix) else ''
    if not token or not hmac.compare_digest(token, config.api_token):
        return False
    return True
