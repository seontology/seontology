#!/bin/bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

if $(git diff HEAD~1 --exit-code "$SCRIPT_DIR/../seovoc.owl" > /dev/null); then
    echo "seovoc.owx not changed."
else
    echo "seovoc.owx changed, regenerating owl and tll files."

    $SCRIPT_DIR/robot convert --input "$SCRIPT_DIR/../seovoc.owx" --format owl --output "$SCRIPT_DIR/../seovoc.owl"
    $SCRIPT_DIR/robot convert --input "$SCRIPT_DIR/../seovoc.owx" --format ttl --output "$SCRIPT_DIR/../seovoc.ttl"

    git commit -m "update seovoc.owl and seovoc.ttl" $SCRIPT_DIR/../seovoc.owl $SCRIPT_DIR/../seovoc.ttl

    echo "*** Pushing changes..."
    git push
fi