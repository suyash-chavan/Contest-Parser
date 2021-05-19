#!/bin/bash
# This script will created necessary files.
# Version: 2.0


if [ $(id -u) != "0" ]; then
echo "You must be the superuser to run this script" 
exit 1
fi

FOLDER=/etc/contest-parser/

if [ ! -f "$FOLDER" ]; then
	echo "Folder Already Exists!"
else
	mkdir "$FOLDER"
    echo "Creted Contest-Parser folder!"
fi

echo "Updating Judge!"
cp judge.py /etc/contest-parser/judge.py


FILE=/etc/contest-parser/settings.json
if test -f "$FILE"; then
    echo "$FILE exists."
else
	cp settings.json /etc/contest-parser/settings.json
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
