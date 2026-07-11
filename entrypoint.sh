#!/bin/sh
set -e

addgroup -g "$PGID" appuser
adduser -D -u "$PUID" -G appuser appuser

chown appuser:appuser /dev/uinput

exec su-exec appuser "$@"
