# 📺 Python Web Remote Control

A lightweight web-based remote control for TV/streaming boxes. Built to control a Linux streaming box where the on-screen UI needed to be navigated with arrow keys.

![screenshot](images/screenshot.webp)

## Features

- Control a device's UI (arrow key navigation, etc.) from any browser on your network
- Simple installation via `pip` or Docker
- Runs a lightweight web server on port `8080`

## Requirements

- Python 3.x
- `pip` and `venv` (for bare metal installation)
- Docker and Docker Compose (for containerized installation)

## Installation

### Bare metal

Create a virtual environment and install the package into it:

```bash
python -m venv venv
source venv/bin/activate
pip install .
```

### Docker

Edit `docker-compose.yml` to suit your setup, then bring up the container:

```bash
docker compose up -d
```

## Usage

Run the program from the terminal:

```bash
web-tv-remote-control
```

Once running, open a browser and navigate to port `8080` on the host machine:

```
http://<host-ip>:8080
```

## Contributing

Issues and pull requests are welcome!
