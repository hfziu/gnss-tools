# -*- coding: utf-8 -*-

import math
import blh2xyz
import numpy as np

def xyz2neu(x, y, z, B, L, H):
    [x_st, y_st, z_st] = blh2xyz.blh2xyz(B, L, H)
    B = B / 180 * math.pi
    L = L / 180 * math.pi
    T = np.mat([[-1*math.cos(L)*math.sin(B), -1*math.sin(L)*math.sin(B), math.cos(B)],
                [-1*math.sin(L), math.cos(L), 0],
                [math.cos(L)*math.cos(B), math.sin(L)*math.cos(B), math.sin(B)]])
    XYZ = np.mat([[x-x_st],[y-y_st],[z-z_st]])
    NEU = np.dot(T, XYZ)

    return [NEU.item(0), NEU.item(1), NEU.item(2)]
