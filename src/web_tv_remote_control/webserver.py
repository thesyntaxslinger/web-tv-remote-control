from flask import Flask, send_from_directory, request
from .keys import press
from .api import send_key_to_api, verify_api_key
from .config import config


def create_app(mode):
    app = Flask(__name__)

    if mode == 'both':
        print('RUNNING IN NORMAL BOTH MODE')
        @app.route('/')
        def index():
            return send_from_directory('web', 'both.html')

        @app.route('/<path:path>')
        def files(path):
            return send_from_directory('web', path)

        @app.route('/key/<button>', methods=['POST'])
        def buttonpress(button):
            response = press(button)
            if not response:
                return 'Bad request', 400
            return 'OK'


    elif mode == 'api':
        print('RUNNING IN API MODE')
        @app.route('/key/<button>', methods=['POST'])
        def buttonpress(button):
            auth_header = request.headers.get('Authorization', '')
            if not verify_api_key(auth_header):
                return 'Unauthorized', 401
            
            response = press(button)
            if not response:
                return 'Bad request', 400
            return 'OK'


    elif mode == 'controller':
        print('RUNNING IN CONTROLLER MODE')
        @app.route('/')
        def index():
            return send_from_directory('web', 'controller.html')

        @app.route('/<path:path>')
        def files(path):
            return send_from_directory('web', path)

        @app.route('/key/<button>', methods=['POST'])
        def send_key(button):
            response = send_key_to_api(button)
            if not response:
                return 'Bad request', 400
            return 'OK'
    return app


def run_server():
    app = create_app(config.mode)
    app.run(host=config.host, port=config.port)
