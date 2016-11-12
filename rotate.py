# -*- coding: utf-8 -*-

import math
import numpy as np

test = np.mat(np.zeros((3,3)))

def R1(omega):
    return np.mat([[1,0,0],[0,math.cos(omega),math.sin(omega)],[0,-1*math.sin(omega),math.cos(omega)]])

def R2(omega):
    return np.mat([[math.cos(omega),0,-1*math.sin(omega)],[0,1,0],[math.sin(omega),0,math.cos(omega)]])

def R3(omega):
    return np.mat([[math.cos(omega),math.sin(omega),0],[-1*math.sin(omega),math.cos(omega),0],[0,0,1]])

