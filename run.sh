#!/bin/sh

CURRENT_DIR=$(cd $(dirname $0); pwd)
WORKDIR=$(mktemp -d)
PYTHON3="/usr/bin/env python3"
APP="$CURRENT_DIR/BurningChr0me.py"
echo "Activating venv"
. $CURRENT_DIR/venv/bin/activate
echo "Running app"
$PYTHON3 "$APP" $@
