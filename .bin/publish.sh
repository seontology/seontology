#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

echo "Working in $SCRIPT_DIR..."

INITIAL_HASH=$(cat $SCRIPT_DIR/../seovoc.owx.md5)
CURRENT_HASH=$(md5sum $SCRIPT_DIR/../seovoc.owx)

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

    git commit -m "update seovoc.owl and seovoc.ttl and hash file" \
        $SCRIPT_DIR/../seovoc.owx.md5 $SCRIPT_DIR/../seovoc.owl $SCRIPT_DIR/../seovoc.ttl

    echo "*** Pushing changes..."
    git push

fi
