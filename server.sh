#!/bin/bash

export PATH=~/miniconda3/bin:${PATH}
MUD_DIR=~/grpc/
export PYTHONPATH="${MUD_DIR}/game_logic:$PYTHONPATH"

python server.py
