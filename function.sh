#!/bin/zsh
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

FUNC=$1
A=$2
B=$3

FILE="$FUNC-$A-$B.wav"

python function.py "$@"
afplay "$SCRIPT_DIR/$FILE"
