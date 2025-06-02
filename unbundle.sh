#!/bin/sh

CURRENT_DIR=$(cd $(dirname $0); pwd)
WORKDIR=$(mktemp -d)
PYTHON3="/usr/bin/env python3"
$PYTHON3 -m venv venv
echo "Activating venv"
source venv/bin/activate
echo "Installing pycryptodome"
cp $CURRENT_DIR/pycryptodome.tar.gz $WORKDIR
cd $WORKDIR
tar -zxvf pycryptodome.tar.gz
cd pycryptodome
pip install .
cd $CURRENT_DIR
echo "Done"