#!/bin/bash

# Validates seovoc.owx with ROBOT: `robot report` (OBO quality checks) and
# `robot reason` (HermiT, which also rejects anything outside OWL 2 DL).
# Outputs go to build/ so they can be uploaded as CI artifacts.
# Both checks always run; the script fails if either of them fails.

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

mkdir -p "$SCRIPT_DIR/../build"

STATUS=0

echo "*** Running robot report..."
docker run --rm -v "${SCRIPT_DIR}/../:/work" obolibrary/robot \
    robot report --input "/work/seovoc.owx" --fail-on ERROR --output "/work/build/report.tsv" || STATUS=1

echo "*** Running robot reason (HermiT)..."
docker run --rm -v "${SCRIPT_DIR}/../:/work" obolibrary/robot \
    robot reason --input "/work/seovoc.owx" --reasoner hermit --output "/work/build/reasoned.owl" || STATUS=1

exit $STATUS
