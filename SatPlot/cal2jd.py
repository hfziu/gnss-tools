#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Calendar date to JD

Usage:
    cal2jd -y <year> -m <month> -d <day>

Options:
    -y <year>   Year
    -m <month>  Month
    -d <day>    Day
Example:
    gps2cal -y 2016 -m 10 -d 1
'''

from docopt import docopt
import math

def cal2jd(year, month, day):
    if month > 2:
        y = year
        m = month
    else:
        y = year - 1
        m = month + 12

    d = day

    #jd = (math.floor(365.25 * y) - math.floor(y / 100) + math.floor(y / 400) + 30 * m
    #        + math.floor((34 / 57) * (m + 1)) + d + 1721119.5)
    jd = (math.floor( 365.25 * y) + math.floor(30.6001 * ( m + 1)) + d + 1720981.5)

    return jd
    

# Command-line Interface
def cli():
    arguments = docopt(__doc__)
    year = int(arguments.get('-y'))
    month = int(arguments.get('-m'))
    day = int(arguments.get('-d'))
    print(cal2jd(year, month, day))

if __name__ == "__main__":
    cli()

