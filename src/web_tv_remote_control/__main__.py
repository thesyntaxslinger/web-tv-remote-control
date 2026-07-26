from .webserver import run_server
from .cli import parse_args
from .config import config


def main():
    args = parse_args()
    config.load_from_args(args)
    run_server()

if __name__ == '__main__':
    main()
