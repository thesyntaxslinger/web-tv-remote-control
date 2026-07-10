import argparse
from .webserver import run_server
from .cli import make_parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    run_server(args.host, args.port)


if __name__ == '__main__':
    main()
