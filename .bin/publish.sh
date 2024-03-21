#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

echo "Working in $SCRIPT_DIR..."

INITIAL_HASH=$(cat $SCRIPT_DIR/../seovoc.owx.md5)
CURRENT_HASH=$(md5sum $SCRIPT_DIR/../seovoc.owx | awk '{printf $1}')

if [[ "$INITIAL_HASH" == "$CURRENT_HASH" ]]; then
    echo "seovoc.owx unchanged." && exit 0
else
    echo "MD5 hash has changed!"

    echo "*** Configuring git..."
    git config user.name github-actions
    git config user.email github-actions@github.com

    docker run --rm -v "${SCRIPT_DIR}/../:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format owl --output "/work/seovoc.owl"

    docker run --rm -v "${SCRIPT_DIR}/../:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format ttl --output "/work/seovoc.ttl"

    rm $SCRIPT_DIR/../seovoc.owx.md5 && echo $CURRENT_HASH >$SCRIPT_DIR/../seovoc.owx.md5

    git add -A
    git commit -m "automatically update seovoc.owl, seovoc.ttl and seovoc.owx.md5 from seovoc.owx" -a

    echo "*** Pushing changes..."
    git push

fi
