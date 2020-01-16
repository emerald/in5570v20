#!/usr/bin/env python3

import argparse
import os
import shlex
import subprocess

image="portoleks/in5570v20"

workdir = shlex.quote(os.path.dirname(os.path.realpath(__file__)))

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('command', type=str, nargs=1,
                    help='Either interact, start, attach, or stop')

args = parser.parse_args()

if args.command == "interact":
    subprocess.call([
        "docker", "run",
        "--interactive", "--tty", "--rm",
        "--volume", workdir + ":/home/docker/src/",
        "--workdir", "/home/docker/src/",
        image])
