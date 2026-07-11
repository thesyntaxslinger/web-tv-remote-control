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

chown appuser:appuser /dev/uinput >/dev/null 2>&1 

exec su-exec appuser "$@"
