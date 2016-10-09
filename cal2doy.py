#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Calendar date to day-of-year

Usage:
    cal2doy -f <in-file> | -n <day-or-date> [-o <out-file>]

Options:
    -f <in-file>        从文件读取
    -n <day-or-date>    直接输入要转换的数字或日期
    -o <out-file>       输出到文件
    -h                  显示本帮助

Example:
    cal2doy -n 2016-10-01
'''

from docopt import docopt
import re

# Check if 
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

# Convert calendar date to doy
def cal2doy(cal_date):
    ymd_str = cal_date.split('-')
    ymd_int = []
    # Convert strings to integers
    for item in ymd_str:
        ymd_int.append(int(item))
    ymd0 = ['year', 'month', 'day']
    ymd = dict(zip(ymd0, ymd_int))

    months = range(1,13)
    doy_until_last_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    doy_until_last_month = dict(zip(months, doy_until_last_month))

    doy = doy_until_last_month.get(ymd.get('month')) + ymd.get('day')
    doy = (doy + int(is_leap_year(ymd.get('year')))) if ymd.get('month') > 2 else doy

    return doy

# Command-line Interface
def cli():
    arguments = docopt(__doc__)
    #print(arguments)
    if arguments.get('-n'):
        print(cal2doy(arguments.get('-n')))
    elif arguments.get('-f'):
        pass

if __name__ == '__main__':
    cli()

