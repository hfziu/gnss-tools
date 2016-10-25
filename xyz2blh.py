# -*- coding: utf-8 -*-
"""
Convert XYZ to BLH
xcalcor@gmail.com
"""
import math

def xyz2blh(X, Y, Z):
    a = 6378137
    f = 1 / 298.257223653
    e2 = 2 * f - f ** 2
    L = math.atan(Y / X)

    if X < 0:
        L = L + math.pi
    elif Y < 0 and X > 0:
        L = L + 2 * math.pi

    L = L * 180 / math.pi - 180

    B = math.atan(Z / math.sqrt( X ** 2 + Y ** 2))
    B_iterative = 0

    while abs(B - B_iterative) > 1e-11:
        N = a / math.sqrt(1 - e2 * math.sin(B) ** 2)
        H = math.sqrt(X ** 2 + Y ** 2) / math.cos(B) - N
        B_iterative = B
        B = math.atan(Z / math.sqrt(X ** 2 + Y ** 2) / (1 - e2 * N / (N + H)))

    H = Z / math.sin(B) - N * (1 - e2)
    B = B * 180 / math.pi

    return [B, L, H]

