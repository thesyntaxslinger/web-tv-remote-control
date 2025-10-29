# Python Web Remote Control API

Made this to control a streaming box that was running Arch and needed to use the arrow keys to move around the UI on the TV.

![screenshot](images/screenshot.webp)

## Installation

You need a few dependancies for this:

- ydotool
- python-flask

Optionally you can install a webserver and then use basic auth for authentication for security so nobody on your network gets to control your TV.

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

## Security Considerations

DO NOT EXPOSE THIS TO THE INTERNET

Anyone can simply edit the HTML and change what keys to send via ydotool. This was made for a trusted envrionment.
