import argparse
import os

def make_parser():
    parser = argparse.ArgumentParser(
        prog='web-tv-remote-control',
        description='A web-ui to control your PC with a TV remote from another device.'
    )
    parser.add_argument('-H', '--host', default=os.environ.get('HOST', '::'), type=str, help='specifies the host to listen on')
    parser.add_argument('-p', '--port', default=os.environ.get('PORT', 8080), type=int, help='specifies the port to start the webserver with')
    return parser
