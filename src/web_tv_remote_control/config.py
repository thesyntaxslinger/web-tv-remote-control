allowed_keys = {
    "up": 103,
    "down": 108,
    "left": 105,
    "right": 106,
    "back": 1,
    "ok": 28
}
special_keys = {'on', 'off'}

class Config:
    def __init__(self):
        self.allowed_keys = allowed_keys
        self.special_keys = special_keys
        self.host = None
        self.port = None
        self.mode = None
        self.api_token = None
        self.api_url = None

    def load_from_args(self, args):
        self.host = args.host
        self.port = args.port
        self.mode = args.mode
        self.api_token = args.api_token
        self.api_url = args.api_url

config = Config()

"""
TODO:
client.load_host_keys(config.ssh_known_hosts_path)
hostname=config.ssh_host,
port=config.ssh_host,
username=config.ssh_user,
key_filename=config.ssh_key_path,
send_magic_packet(config.macaddress)
"""
