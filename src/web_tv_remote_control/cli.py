import argparse
import os
import secrets


modes = ('controller', 'api', 'both')

def make_api_token():
    token = secrets.token_urlsafe(32)
    return token


def make_parser():
    parser = argparse.ArgumentParser(
        prog='web-tv-remote-control',
        description='A web-ui to control your PC with a TV remote from another device.'
    )
    parser.add_argument('-H', '--host', default=os.environ.get('HOST', '::'), type=str, help='the host to listen on')
    parser.add_argument('-p', '--port', default=os.environ.get('PORT', 8080), type=int, help='the port to listen on')
    parser.add_argument('-m', '--mode', default=os.environ.get('MODE', 'both'), choices=modes, type=str, help='the mode to run %(prog)s in')
    parser.add_argument('--api-token', default=os.environ.get('API_TOKEN'), type=str, help='used for both controller or api')
    parser.add_argument('--config-dir', default=os.environ.get('CONFIG_DIR'), type=str, help='directory that has the config files')
    parser.add_argument('--api-url', default=os.environ.get('API_URL'), type=str, help='the scheme, host, and port (if needed) of the api server')
    parser.add_argument('--api-macaddress', default=os.environ.get('API_MACADDRESS'), type=str, help='mac address of the api server')
    parser.add_argument('--ssh-user', default=os.environ.get('SSH_USER'), type=str, help='SSH user of the api server')
    parser.add_argument('--ssh-host', default=os.environ.get('SSH_HOST'), type=str, help='address or hostname of the api server')
    parser.add_argument('--ssh-port', default=os.environ.get('SSH_PORT'), type=int, help='SSH port of the api server')
    """
    TODO:
    client.load_host_keys(config.ssh_known_hosts_path)
    hostname=config.ssh_host,
    port=config.ssh_host,
    username=config.ssh_user,
    key_filename=config.ssh_key_path,
    send_magic_packet(config.macaddress)
    """
    return parser

def validate_args(parser, args):
    if args.mode == 'controller':
        missing = [
            name for name, value in (
                ('--api-token', args.api_token),
                ('--api-url', args.api_url),
                ('--config-dir', args.config_dir),
                ('--api-macaddress', args.api_macaddress),
                ('--ssh-user', args.ssh_user),
                ('--ssh-host', args.ssh_host),
                ('--ssh-port', args.ssh_port)
            )
            if not value
        ]
        if missing:
            parser.error(
                f"mode 'controller' requires: {', '.join(missing)}"
            )
    elif args.mode == 'api':
        missing = [
            name for name, value in (
                ('--api-token', args.api_token),
            )
            if not value
        ]
        if missing:
            token = make_api_token()
            args.api_token = token
            print("=============================================")
            print("This token is not persistent and will change.")
            print("Please save it to your environment")
            print(token)
            print("=============================================")
        found = [
            name for name, value in (
                ('--api-url', args.api_url),
                ('--config-dir', args.config_dir),
                ('--api-macaddress', args.api_macaddress),
                ('--ssh-user', args.ssh_user),
                ('--ssh-host', args.ssh_host),
                ('--ssh-port', args.ssh_port)
            )
            if value
        ]
        if found:
            print("WARN: Environment variables found for controller but ignoring due to mode set to 'api'")
    elif args.mode == 'both':
        found = [
            name for name, value in (
                ('--api-token', args.api_token),
                ('--api-url', args.api_url),
                ('--config-dir', args.config_dir),
                ('--api-macaddress', args.api_macaddress),
                ('--ssh-user', args.ssh_user),
                ('--ssh-host', args.ssh_host),
                ('--ssh-port', args.ssh_port)
            )
            if value
        ]
        if found:
            print("WARN: Environment variables found for controller/api but ignoring due to mode set to 'both'")



def parse_args(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)
    validate_args(parser, args)
    return args
