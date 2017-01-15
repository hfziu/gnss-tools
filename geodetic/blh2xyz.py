#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Converts geodetic coordinates [B,L,H] to cartesian coordinates [X,Y,Z]
author:essethon
xcalcor@gmail.com
MIT License

Usage:
    blh2xyz -e <ellipsoid> <B> <L> <H>

Options:
    -e <ellipsoid>  name of a particular reference ellipsoid

Example:
    blh2xyz -e 'WGS84' 50 50 0
"""

import math
from docopt import docopt

from geo_ellipsoid import geo_ellipsoid


def blh2xyz(ell, B, L, H):
    a = geo_ellipsoid(ell).a
    e2 = geo_ellipsoid(ell).e2
    N = a / math.sqrt(1 - e2 * math.sin(B) ** 2)
    L = L / 180 * math.pi
    B = B / 180 * math.pi

    X = (N + H) * math.cos(B) * math.cos(L)
    Y = (N + H) * math.cos(B) * math.sin(L)
    Z = (N * (1 - e2) + H) * math.sin(B)

    return [X, Y, Z]


def cli():
    arguments = docopt(__doc__)
    # print(arguments)
    ell = arguments.get('-e')
    B = float(arguments.get('<B>'))
    L = float(arguments.get('<L>'))
    H = float(arguments.get('<H>'))
    print(blh2xyz(ell, B, L, H))

if __name__ == "__main__":
    cli()
