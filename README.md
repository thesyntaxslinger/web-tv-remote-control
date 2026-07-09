# Python Web Remote Control API

Made this to control a streaming box that was running Arch and needed to use the arrow keys to move around the UI on the TV.

![screenshot](images/screenshot.webp)

## Installation

Make a venv then install all the deps

```bash
python -m venv venv
source venv/bin/activate
pip install .
```

```bash
sudo usermod -aG input user
```

## Usage

To run the program just call it from the terminal

```bash
web-tv-remote-control
```

Then you can access it on port 8080 of the machine you are running it on.

## To-Do
1. Arg parse things so users can specify ports 
2. Make Dockerfile once step 1 is complete
