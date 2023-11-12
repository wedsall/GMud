#!/bin/bash

MUD_DIR=~/grpc/
export PYTHONPATH="${MUD_DIR}/game_logic:$PYTHONPATH"

python server.py
