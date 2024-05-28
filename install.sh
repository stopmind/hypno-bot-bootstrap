#!/bin/env sh

hypno_path = "~/hypno-bot"
read -p "Where do you want to store HypnoBot:" hypno_path

mkdir $hypno_path
cd $hypno_path

git clone https://github.com/stopmind/hypno-bot-bootstrap
mv -r hypno-bot-bootstrap bootstrap

chmod +x ./bootstrap/main.py ./bootstrap/runner.py
ln -s ./bootstrap/main.py bot

./bot install
