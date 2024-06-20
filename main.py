#!/bin/env python

from argparse import ArgumentParser
import os, os.path, shutil

cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")

def subcommand(args=[], parent=subparsers):
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
    return decorator

def build():
    if os.path.exists("./build/hypno-bot"):
        os.remove("./build/hypno-bot")

    os.chdir("./hypno-bot")
    os.system("go build -o  ../build")    
    os.chdir("..")

@subcommand()
def install(args):
    os.system("git clone https://github.com/stopmind/hypno-bot/")
    os.mkdir("build")
    os.mkdir("build/log")
    os.mkdir("build/storage")
    build()

    print("Please create build/config.toml")

@subcommand()
def update(args):
    shutil.rmtree("bootstrap")
    shutil.rmtree("hypno-bot")

    os.system("git clone https://github.com/stopmind/hypno-bot/")
    os.system("git clone https://github.com/stopmind/hypno-bot-bootstrap/")

    os.rename("hypno-bot-bootstrap", "bootstrap")

    build()

@subcommand()
def run(args):
    if os.path.exists("runner-pipe"):
        print("bot already active")
        return
    os.system("nohup ./bootstrap/runner.py &")

@subcommand()
def stop(args):
    if not os.path.exists("runner-pipe"):
        print("bot isn't active")
        return
    
    os.system("echo stop > runner-pipe")

@subcommand()
def restart(args):
    os.system("echo stop > runner-pipe")
    os.system("nohup ./bootstrap/runner.py &")

if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)