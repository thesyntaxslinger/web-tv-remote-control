from pathlib import Path
import sys

allowed_keys = {
    "up": 103,
    "down": 108,
    "left": 105,
    "right": 106,
    "back": 1,
    "ok": 28
}
special_keys = {'on', 'off'}

def get_vars_from_config_dir(mode, config_dir):
    if mode != 'controller':
        return None
    if not Path(config_dir).is_dir():
        raise NotADirectoryError(f"{config_dir} does not exist or is not a directory")
        sys.exit(1)

    ssh_known_hosts = config_dir + '/known_hosts'
    ssh_key = config_dir + '/id_ed25519'

    if not Path(ssh_known_hosts).is_file():
        print(f"{ssh_known_hosts} does not exist")
        sys.exit(1) 
    if not Path(ssh_key).is_file():
        print(f"{ssh_key} does not exist")
        sys.exit(1)
    return ssh_known_hosts, ssh_key


class Config:
    def __init__(self):
        self.allowed_keys = allowed_keys
        self.special_keys = special_keys
        self.host = None
        self.port = None
        self.mode = None
        self.api_token = None
        self.api_url = None
        self.config_dir = None
        self.api_macaddress = None
        self.ssh_user = None
        self.ssh_host = None
        self.ssh_port = None
        self.ssh_known_hosts = None
        self.ssh_key = None

    def load_from_args(self, args):
        self.host = args.host
        self.port = args.port
        self.mode = args.mode
        self.api_token = args.api_token
        self.api_url = args.api_url
        self.config_dir = args.config_dir
        self.api_macaddress = args.api_macaddress
        self.ssh_user = args.ssh_user
        self.ssh_host = args.ssh_host
        self.ssh_port = args.ssh_port

        ssh_vars = get_vars_from_config_dir(self.mode, self.config_dir)
        if ssh_vars is not None:
            self.ssh_known_hosts, self.ssh_key = ssh_vars

config = Config()
