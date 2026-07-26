allowed_keys = {
    "up": 103,
    "down": 108,
    "left": 105,
    "right": 106,
    "back": 1,
    "ok": 28
}

class Config:
    def __init__(self):
        self.allowed_keys = allowed_keys
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
