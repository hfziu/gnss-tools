#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Convert day-of-year to calendar date 

Usage:
    doy2cal -y <year> -d <day-of-year>

Options:
    -y <year>           年份
    -d <day-of-year>    年积日
    -h                  显示本帮助

Example:
    doy2cal -y 2016 -d 275
'''

from docopt import docopt
from is_leap_year import is_leap_year

# Convert calendar date to doy
def doy2cal(year, doy):
    if is_leap_year(year):
        doy_until_last_month = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    else:
        doy_until_last_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    # Search
    for i, dulm in enumerate(doy_until_last_month):
        if doy <= dulm:
            month = i
            day = doy - doy_until_last_month[i-1]
            break


    return [year, month, day]

# Command-line Interface
def cli():
    arguments = docopt(__doc__)
    cal = doy2cal(int(arguments.get('-y')), int(arguments.get('-d')))
    cal = '-'.join([str(cal[0]), str(cal[1]), str(cal[2])])
    print(cal)

if __name__ == '__main__':
    cli()

