#!/bin/sh
set -e

# create group if it doesn't already exist
if ! getent group "$PGID"; then
    addgroup -g "$PGID" appuser
fi

# create user if it doesn't already exist
if ! getent passwd "$PUID"; then
    adduser -D -u "$PUID" -G appuser appuser
fi

# uinput is only needed when this container actually presses keys locally
if [ "$MODE" != "controller" ]; then
    if [ -e /dev/uinput ]; then
        chown appuser:appuser /dev/uinput
    else
        echo "WARNING: MODE=$MODE requires /dev/uinput but it was not found. Did you forget to mount it?" >&2
    fi
fi

exec su-exec appuser "$@"
