#!/usr/bin/python3

import os
from flask import Flask, request, render_template_string, send_from_directory
import subprocess

app = Flask(__name__)

# HTML Remote Interface
HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Remote</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="icon" type="image/x-icon" href="/assets/icons/favicon.ico">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/icons/favicon-48.png">
  <link rel="apple-touch-icon" sizes="192x192" href="/assets/icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/assets/icons/icon-512.png">
  <link rel="icon" type="image/png" sizes="512x512" href="/assets/icons/icon-512-maskable.png">
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#000000">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">

  <style>
    body {
      background-color: #121212;
      margin: 0;
      padding: 2rem;
      font-family: sans-serif;
      display: flex;
      justify-content: center;
    }
    .container {
      width: 100%;
      max-width: 400px;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .full-width {
      width: 100%;
      height: 160px;
      font-size: 2rem;
    }
    .half-row {
      display: flex;
      gap: 1rem;
    }
    .half {
      flex: 1;
      height: 160px;
      font-size: 2rem;
    }
    button {
      background-color: #1e1e1e;
      color: #fff;
      border: none;
      border-radius: 12px;
      touch-action: manipulation;
    }
    button:active {
      background-color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <button class="full-width" onclick="sendKey('103')">▲</button>

    <div class="half-row">
      <button class="half" onclick="sendKey('105')">◀</button>
      <button class="half" onclick="sendKey('106')">▶</button>
    </div>

    <button class="full-width" onclick="sendKey('108')">▼</button>

    <div class="half-row">
      <button class="half" onclick="sendKey('1')">Back</button>
      <button class="half" onclick="sendKey('28')">OK</button>
    </div>
  </div>

  <script>
    function sendKey(key) {
      fetch('/key?k=' + key).catch(e => console.log(e));
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

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/icons/<path:filename>')
def assets(filename):
    return send_from_directory('./assets/icons', filename)

@app.route('/manifest.json')
def manifest():
    return send_from_directory('./assets', 'manifest.json')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('./assets', 'sw.js')

@app.route('/key')
def keypress():
    key = request.args.get('k', '')

    if key.isdigit():
        key_sequence = f"{key}:1 {key}:0"
    else:
        key_sequence = key

    env = os.environ.copy()
    env['YDOTOOL_SOCKET'] = '/run/user/1000/.ydotool_socket'

    subprocess.run(
        ['ydotool', 'key'] + key_sequence.split(),
        env=env,
        timeout=2
    )

    return 'OK'

if __name__ == '__main__':
    app.run(host='::', port=8080)
