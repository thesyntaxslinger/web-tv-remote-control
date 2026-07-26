from evdev import UInput, ecodes as e
#from wakeonlan import send_magic_packet

from .config import config
#from .ssh import ssh_api_and_turn_off


_ui = None

def _get_uinput():
    global _ui
    if _ui is None:
        _ui = UInput({e.EV_KEY: list(e.keys.keys())}, name='python-evdev-vkbd')
    return _ui


def press(request):
    if request not in config.allowed_keys and request not in config.special_keys:
        return False

    if request in config.allowed_keys:
        send_code(config.allowed_keys[request])
        return True

#    if request in config.special_keys:
#        if request == 'on' and config.mode == 'controller':
#            send_magic_packet(config.macaddress)
#            return True
#        if request == 'off' and config.mode == 'controller':
#            # command="/sbin/poweroff",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ssh-ed25519 AAA...
#            ssh_api_and_turn_off()
#            return True

    return False

        


def send_code(code):
    ui = _get_uinput()
    ui.write(e.EV_KEY, code, 1)  # key down
    ui.write(e.EV_KEY, code, 0)  # key up
    ui.syn()                     # flush the event
