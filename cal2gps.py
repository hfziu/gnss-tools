#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Calendar datetime to JD, FOD, GPSW, DOW and SOW

Usage:
    cal2gps -c <cal> --hr <hour> --min <minute> --sec <second>

Options:
    -c <cal>        Calendar Date
    --hr <hour>     Hour
    --min <minute>  Minute
    --sec <second>  Second
Example:
    cal2gps -c 2016-10-1 --hr 22 --min 23 --sec 24
'''

from docopt import docopt
import math
from cal2jd import cal2jd
from cal2doy import cal2doy

def cal2gps(year, month, day, hour, minute, second):
    JD = cal2jd(year, month, day)
    FOD = hour / 24 + minute / 1440 + second / 86400
    GPSW = math.floor((JD - cal2jd(1980, 1, 6)) / 7)
    DOW = math.floor((JD + 1.5) % 7)
    SOW = DOW * 86400 + hour * 3600 + minute * 60 + second
    DOY = cal2doy('-'.join([str(year), str(month), str(day)]))

    keys = ['JD', 'FOD', 'GPSW', 'DOW', 'SOW', 'DOY']
    values = [JD, FOD, GPSW, DOW, SOW, DOY]
    return dict(zip(keys, values))
    

# Command-line Interface
def cli():
    arguments = docopt(__doc__)
    #print(arguments)
    ymd_str = arguments.get('-c').split('-')
    year = int(ymd_str[0])
    month = int(ymd_str[1])
    day = int(ymd_str[2])
    hour = int(arguments.get('--hr'))
    minute = int(arguments.get('--min'))
    second = int(arguments.get('--sec'))
    print(cal2gps(year, month, day, hour, minute, second))


if __name__ == "__main__":
    cli()

