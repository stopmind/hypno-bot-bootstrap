#!/bin/env python

import os, signal

pid = os.fork()
if pid == 0:
    os.chdir("./build")
    os.execl("hypno-bot", "hypno-bot")
    exit()
    
os.mkfifo("runner-pipe")

with open("runner-pipe") as fifo:
    os.kill(pid, signal.SIGTERM)

os.remove("runner-pipe")
exit()
    
