#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
