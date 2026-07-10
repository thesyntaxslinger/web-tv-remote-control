from evdev import UInput, ecodes as e

# make allowed keys
allowed_keys = {
    "up": 103,
    "down": 108,
    "left": 105,
    "right": 106,
    "back": 1,
    "ok": 28
}

# define the UInput write device
_ui = UInput({e.EV_KEY: list(e.keys.keys())}, name='python-evdev-vkbd')


def press(request):
    if request not in allowed_keys:
        return False
    send_code(allowed_keys[request])
    return True

def send_code(code):
    _ui.write(e.EV_KEY, code, 1) # key down
    _ui.write(e.EV_KEY, code, 0) # key up
    _ui.syn()                    # flush the event

