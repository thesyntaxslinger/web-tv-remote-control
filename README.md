# Python Web Remote Control API

Made this to control a streaming box that was running Arch and needed to use the arrow keys to move around the UI on the TV.

![screenshot](images/screenshot.webp)

## Requirements

You need a few dependancies for this:

- ydotool
- python-flask

You can install a webserver and then use basic auth for authentication for security so nobody on your network gets to control your TV.

### Arch Linux

```bash
sudo pacman -Syy ydotool python-flask
```

## Usage

Run this:

```bash
python3 ./web-tv-remote-control.py
```

Then you can access it on port 8080 of the machine you are running it on.

### Running with a systemd units

Python systemd unit:

```systemd
[Unit]
Description=Flask Application
After=network.target

[Service]
Type=simple
User=user
Group=user

ExecStart=python3 /opt/web-tv-remote-control/web-tv-remote-control.py

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

ydotoold systemd unit:

```systemd
[Unit]
Description=ydotool daemon
After=systemd-user-sessions.service

[Service]
Type=simple
User=user
Group=user
ExecStart=/usr/bin/ydotoold -p /run/user/$(id -u user)/.ydotool_socket
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
```

## To Do

1. Figure out a way to make this no longer use ydotool
2. Make Dockerfile once step 1 is complete
