#!/usr/bin/python3

import os
from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# HTML Remote Interface
HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Remote</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
</body>
</html>

'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/key')
def keypress():
    key = request.args.get('k', '')

    if key.isdigit():
        key_sequence = f"{key}:1 {key}:0"
    else:
        key_sequence = key

    env = os.environ.copy()
    env['YDOTOOL_SOCKET'] = '/run/user/1000/.ydotool_socket'

    subprocess.run(['ydotool', 'key'] + key_sequence.split(), env=env, timeout=2)

    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
