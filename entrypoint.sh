#!/bin/sh
set -e

# create group if it doesn't already exist
if ! getent group "$PGID"; then
    addgroup -g "$PGID" appuser
    # addgroup --gid "$PGID" appuser
fi

# create user if it doesn't already exist
if ! getent passwd "$PUID"; then
    adduser -D -u "$PUID" -G appuser appuser
    # useradd --uid "$PUID" --gid "$PGID" --no-create-home --shell /bin/sh appuser
fi

# uinput is only needed when this container actually presses keys locally
if [ "$MODE" != "controller" ]; then
    if [ -e /dev/uinput ]; then
        chown appuser:appuser /dev/uinput
    else
        echo "WARNING: MODE=$MODE requires /dev/uinput but it was not found. Did you forget to mount it?" >&2
    fi
fi


# config dir is only required for controller mode (ssh known_hosts + private key)
if [ "$MODE" = "controller" ]; then
    # set var in here as workaround for cli.py checks
    CONFIG_DIR="${CONFIG_DIR:-/config}"
    export CONFIG_DIR

    if [ ! -d "$CONFIG_DIR" ]; then
        echo "ERROR: MODE=controller requires $CONFIG_DIR to be mounted, but it was not found." >&2
        echo "Did you forget: -v /host/path/to/config:$CONFIG_DIR ?" >&2
        exit 1
    fi

    if [ ! -f "$CONFIG_DIR/id_ed25519" ] || [ ! -f "$CONFIG_DIR/known_hosts" ]; then
        echo "ERROR: $CONFIG_DIR is mounted but missing id_ed25519 and/or known_hosts." >&2
        exit 1
    fi

    ## OMMITTED due to wanting to run the copy and paste to set the perms first, then we can mount with :ro
    # appuser needs to read these at runtime — fix ownership since the
    # mounted host dir is very likely owned by the host user, not appuser
    #chown -R appuser:appuser "$CONFIG_DIR"
    #chmod 600 "$CONFIG_DIR/id_ed25519"
    #chmod 600 "$CONFIG_DIR/known_hosts"
else
    if [ -d "$CONFIG_DIR" ]; then
        echo "WARN: MODE=$MODE does not use $CONFIG_DIR, but it is mounted. Ignoring it." >&2
    fi
fi


exec su-exec appuser "$@"
# exec gosu appuser "$@"
