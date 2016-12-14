# -*- coding:utf-8 -*-

"""
Convert from BLH to XYZ
xcalcor@gmail.com
MIT License
"""
import math

def blh2xyz(B, L, H):
    a = 6378137
    f = 1/298.257223563
    e2 = 2 * f - f ** 2
    N = a / math.sqrt( 1 - e2 * math.sin(B) ** 2)
    L = L / 180 * math.pi
    B = B / 180 * math.pi

    X = (N + H) * math.cos(B) * math.cos(L)
    Y = (N + H) * math.cos(B) * math.sin(L)
    Z = (N * (1 - e2) + H) * math.sin(B)

    return [X, Y, Z]
