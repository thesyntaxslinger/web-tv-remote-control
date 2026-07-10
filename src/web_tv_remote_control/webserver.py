from flask import Flask, send_from_directory
from .keys import press

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

@app.route('/<path:path>')
def files(path):
    return send_from_directory('web', path)


@app.route('/key/<button>', methods=['POST'])
def buttonpress(button):
    response = press(button)
    if not response:
        return 'Bad request', 400
    return 'OK'


def run_server(host, port):
    app.run(host=host, port=port)
