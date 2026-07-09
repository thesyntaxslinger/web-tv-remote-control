#!/usr/bin/python3

import os
from flask import Flask, request, render_template_string, send_from_directory
from evdev import UInput, ecodes as e
import subprocess

app = Flask(__name__)

# HTML Remote Interface
HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Remote</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="icon" type="image/x-icon" href="/icons/favicon.ico">
  <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/icons/favicon-48.png">
  <link rel="apple-touch-icon" sizes="192x192" href="/icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/icons/icon-512.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/icons/icon-512-maskable.png">
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#ffffff">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="white">
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <div class="container">
    <button class="full-width" onclick="sendKey('up')">▲</button>

    <div class="half-row">
      <button class="half" onclick="sendKey('left')">◀</button>
      <button class="half" onclick="sendKey('right')">▶</button>
    </div>

    <button class="full-width" onclick="sendKey('down')">▼</button>

    <div class="half-row">
      <button class="half" onclick="sendKey('back')">Back</button>
      <button class="half" onclick="sendKey('ok')">OK</button>
    </div>
  </div>

  <script>
    function sendKey(action) {
      fetch('/key/' + action, { method: 'POST' }).catch(e => console.log(e));
    }
  </script>
  <script>
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js");
  }
  </script>
</body>
</html>

'''

_ui = UInput({e.EV_KEY: list(e.keys.keys())}, name='python-evdev-vkbd')
def send_key(code):
    _ui.write(e.EV_KEY, code, 1)  # key down
    _ui.write(e.EV_KEY, code, 0)  # key up
    _ui.syn()                    # flush the event


@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/icons/<path:filename>')
def assets(filename):
    return send_from_directory('./assets/icons', filename)

@app.route('/manifest.json')
def manifest():
    return send_from_directory('./assets', 'manifest.json')

@app.route('/style.css')
def style():
    return send_from_directory('./assets', 'style.css')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('./assets', 'sw.js')

@app.route('/key/up', methods=['POST'])
def key_up():
    send_key(103)
    return 'OK'

@app.route('/key/left', methods=['POST'])
def key_left():
    send_key(105)
    return 'OK'

@app.route('/key/right', methods=['POST'])
def key_right():
    send_key(106)
    return 'OK'

@app.route('/key/down', methods=['POST'])
def key_down():
    send_key(108)
    return 'OK'

@app.route('/key/back', methods=['POST'])
def key_back():
    send_key(1)
    return 'OK'

@app.route('/key/ok', methods=['POST'])
def key_ok():
    send_key(28)
    return 'OK'

if __name__ == '__main__':
    app.run(host='::', port=8080)
