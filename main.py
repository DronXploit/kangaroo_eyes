#!/usr/bin/env python3
from colorama import init
init()  # Initialize colorama first

from kangaroo_eyes.cli import KangarooCLI

def main():
    cli = KangarooCLI()
    cli.run()

if __name__ == "__main__":
    main()