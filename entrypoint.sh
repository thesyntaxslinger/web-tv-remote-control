#!/bin/sh
set -e

addgroup -g "$PGID" appuser >/dev/null 2>&1
adduser -D -u "$PUID" -G appuser appuser >/dev/null 2>&1

chown appuser:appuser /dev/uinput >/dev/null 2>&1 

exec su-exec appuser "$@"
