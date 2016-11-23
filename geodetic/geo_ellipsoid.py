# -*- coding: utf-8 -*-

"""
Function geo_ellipsoid returns the semi-major axis, flattening and other parameters for
a particular reference ellipsoid.
"""
import math

class Ellipsoid:
    def __init__(self, a, reciprocal_f):
        self.a = a
        self.f = 1/reciprocal_f
        self.e2 = 1 - (1 - self.f) ** 2
        self.omega = 7292115e-11 # rad/s
        self.mu = 3.986004418e14 # m3/s2

def geo_ellipsoid(ell):
    try:
        if ell == "Krasovsky":
            return Ellipsoid(6378245.0, 298.2997381)
        elif ell == "IUGG75" or ell == "IUGG-75":
            return Ellipsoid(6378140.0, 298.257)
        elif ell == "WGS84":
            return Ellipsoid(6378137.0, 298.257223563)
        elif ell == "CGCS2000":
            return Ellipsoid(6378137.0, 298.257222101)
        else:
            raise NameError("Reference ellipsoid %s not found." % ell)
    except NameError:
        raise
