#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

if $(git diff HEAD~1 --exit-code "$SCRIPT_DIR/../seovoc.owl" > /dev/null); then
    echo "seovoc.owx not changed."
else
    echo "seovoc.owx changed, regenerating owl and tll files."

    docker run --rm -v "${SCRIPTDIR}:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format owl --output "/work/seovoc.owl"

    docker run --rm -v "${SCRIPTDIR}:/work" obolibrary/robot \
        robot convert --input "/work/seovoc.owx" --format ttl --output "/work/seovoc.ttl"

    git commit -m "update seovoc.owl and seovoc.ttl" $SCRIPT_DIR/../seovoc.owl $SCRIPT_DIR/../seovoc.ttl

    echo "*** Pushing changes..."
    git push
fi