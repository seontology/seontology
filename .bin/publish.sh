#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

if $(git diff HEAD~1 --exit-code "$SCRIPT_DIR/../seovoc.owl" > /dev/null); then
    echo "seovoc.owx not changed." && exit 0
else
    echo "seovoc.owx changed, regenerating owl and tll files."

    echo "*** Configuring git..."
    git config user.name github-actions
    git config user.email github-actions@github.com

    docker run --rm -v "${SCRIPTDIR}:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format owl --output "/work/seovoc.owl"

    docker run --rm -v "${SCRIPTDIR}:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format ttl --output "/work/seovoc.ttl"

    git commit -m "update seovoc.owl and seovoc.ttl" $SCRIPT_DIR/../seovoc.owl $SCRIPT_DIR/../seovoc.ttl

    echo "*** Pushing changes..."
    git push
fi