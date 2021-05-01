#!/bin/bash
# This script will install dependencies that are required.
# Version: 2.0


if [ $(id -u) != "0" ]; then
echo "You must be the superuser to run this script" >&2
exit 1
fi

pip3 install regex

pip3 install prettytable

pip3 install termcolor

chmod +x build.sh

./build.sh