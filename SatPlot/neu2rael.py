# -*- coding: utf-8 -*-

import math

def neu2rael(N, E, U):
    R0 = math.sqrt(N ** 2 + E ** 2 + U ** 2)
    EL = math.asin(U / R0)

    if EL > 0:
        A = math.atan(E / N)
        if N < 0:
            A = A + math.pi
        elif E < 0 and N > 0:
            A = A + 2 * math.pi
        R = R0

    else:
        A = 0
        R = 0

    return [R, A, EL]
