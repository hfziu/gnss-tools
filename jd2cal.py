#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''GPS week and sow(second of week) to calendar datetime

Usage:
    gps2cal -w <week> -s <sow>

Options:
    -w <week>   GPS week
    -s <sow>    Second of week
    -h          Show help screen

Example:
    gps2cal -w 1446 -s 121800
'''

from docopt import docopt

# Command-line Interface
def cli():
    arguments = docopt(__doc__)
    pass

if __name__ == "__main__":
    cli()

