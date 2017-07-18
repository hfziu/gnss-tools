#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Converts cartesian coordinates [X,Y,Z] to geodetic coordinates [B,L,H]
author:essethon
xcalcor@gmail.com
MIT License

Usage:
    xyz2blh -e <ellipsoid> <X> <Y> <Z>

Options:
    -e <ellipsoid> name of a particular reference ellipsoid

Example:
    xyz2blh -e 'WGS84' 2635900.00704062 3141343.303109762 4854346.770748904

"""
import math
from docopt import docopt

from .geo_ellipsoid import geo_ellipsoid


def xyz2blh(ell, X, Y, Z):
    a = geo_ellipsoid(ell).a
    e2 = geo_ellipsoid(ell).e2

    L = math.atan(Y / X)

    if X < 0:
        L = L + math.pi
    elif Y < 0 and X > 0:
        L = L + 2 * math.pi

    L = L * 180 / math.pi - 180

    B = math.atan(Z / math.sqrt(X ** 2 + Y ** 2))
    B_iterative = 0

    while abs(B - B_iterative) > 1e-11:
        N = a / math.sqrt(1 - e2 * math.sin(B) ** 2)
        H = math.sqrt(X ** 2 + Y ** 2) / math.cos(B) - N
        B_iterative = B
        B = math.atan(Z / math.sqrt(X ** 2 + Y ** 2) / (1 - e2 * N / (N + H)))

    H = Z / math.sin(B) - N * (1 - e2)
    B = B * 180 / math.pi

    return [B, L, H]


def cli():
    arguments = docopt(__doc__)
    # print(arguments)
    ell = arguments.get('-e')
    X = float(arguments.get('<X>'))
    Y = float(arguments.get('<Y>'))
    Z = float(arguments.get('<Z>'))
    print(xyz2blh(ell, X, Y, Z))

if __name__ == "__main__":
    cli()
