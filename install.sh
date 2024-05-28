#!/bin/env sh

HYPNO=""
read -p "Where do you want to store HypnoBot? (full path): " HYPNO

mkdir -p $HYPNO
cd $HYPNO

git clone https://github.com/stopmind/hypno-bot-bootstrap
mv hypno-bot-bootstrap bootstrap

chmod +x ./bootstrap/main.py ./bootstrap/runner.py
ln -s ./bootstrap/main.py bot

./bot install
