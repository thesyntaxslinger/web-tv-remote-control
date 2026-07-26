from evdev import UInput, ecodes as e
from .config import config


_ui = None

def _get_uinput():
    global _ui
    if _ui is None:
        _ui = UInput({e.EV_KEY: list(e.keys.keys())}, name='python-evdev-vkbd')
    return _ui


def press(request):
    if request not in config.allowed_keys:
        return False
    send_code(config.allowed_keys[request])
    return True

def send_code(code):
    ui = _get_uinput()
    ui.write(e.EV_KEY, code, 1)  # key down
    ui.write(e.EV_KEY, code, 0)  # key up
    ui.syn()                     # flush the event
