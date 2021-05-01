#!/bin/bash
# This script will created necessary files.
# Version: 2.0


if [ $(id -u) != "0" ]; then
echo "You must be the superuser to run this script" >&2
exit 1
fi

FOLDER=/etc/contest-parser/

if [ ! -f "$FOLDER" ]; then
	echo "Folder Already Exists!"
else
	mkdir "$FOLDER"
    echo "Creted Contest-Parser folder!"
fi


CODECHEF=/etc/contest-parser/Codechef
echo "Updating Codechef Files!"
rm -rf "$CODECHEF"
mkdir "$CODECHEF"
cp -R Codechef "$FOLDER"

CODEFORCES=/etc/contest-parser/Codeforces
echo "Updating Codeforces Files!"
rm -rf "$CODEFORCES"
mkdir "$CODEFORCES"
cp -R Codeforces "$FOLDER"
