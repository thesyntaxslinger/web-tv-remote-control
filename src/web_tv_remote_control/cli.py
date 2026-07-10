import argparse

def make_parser():
    parser = argparse.ArgumentParser(
        prog='web-tv-remote-control',
        description='makes a web ui to control your computer with a tv remote from your phone'
    )
    parser.add_argument('-H', '--host', default='::', type=str, help='specifies the host to listen on')
    parser.add_argument('-p', '--port', default=8080, type=int, help='specifies the port to start the webserver with')
    return parser
