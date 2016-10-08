#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''年月日与年积日转换

Usage:
    doy (-d | -D) (-f <file> | -n <day-or-date>)

Options:
    -d, --day   转换为年积日
    -D, --date  转换为日期
    -f, --file  从文件读取
    -n          直接输入要转换的数字或日期

Example:
    doy -d -n 2016-10-01
'''

from docopt import docopt

def doy():
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    doy()

