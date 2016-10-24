# -*- coding: utf-8 -*-

from cal2gps import cal2gps
from spos import spos
from rinex import readRinexNav

import math
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def traceECEF(prn):
    # Get Data
    df = readRinexNav.readRinexNav('./brdc2750.16n', prn)
    
    # Temp: Use data at 12:00:00
    T_r = 7

    # Set Parameters
    t_oe = df['TimeEph'][T_r]
    M_0 = df['M0'][T_r]
    Delta_n = df['DeltaN'][T_r]
    sqrt_a = df['sqrtA'][T_r]
    e = df['Eccentricity'][T_r]
    omega = df['omega'][T_r]
    Cuc = df['Cuc'][T_r]
    Cus = df['Cus'][T_r]
    Crc = df['Crc'][T_r]
    Crs = df['Crs'][T_r]
    Cic = df['Cic'][T_r]
    Cis = df['Cis'][T_r]
    i_0 = df['Io'][T_r]
    OMEGA_0 = df['OMEGA'][T_r]
    i_dot = df['IDOT'][T_r]
    OMEGA_DOT = df['OMEGA DOT'][T_r]



    # Initialization
    x_ECEF = []
    y_ECEF = []
    z_ECEF = []
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    # Calculate
    for t in range(518400, 604800, 300):
        xyz_ECEF = spos(t, t_oe, M_0, Delta_n, sqrt_a, e, omega, Cuc, Cus, Crc, Crs, Cic, Cis, i_0, OMEGA_0, i_dot, OMEGA_DOT)
        #x_ECEF.append(xyz_ECEF.item(0))
        #y_ECEF.append(xyz_ECEF.item(1))
        #z_ECEF.append(xyz_ECEF.item(2))
        #print([xyz_ECEF.item(0),xyz_ECEF.item(1),xyz_ECEF.item(2)])
        ax.scatter(xyz_ECEF.item(0), xyz_ECEF.item(1), xyz_ECEF.item(2), s=1)

    # Plot
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x=6371000 * np.cos(u)*np.sin(v)
    y=6371000 * np.sin(u)*np.sin(v)
    z=6371000 * np.cos(v)
    ax.plot_wireframe(x, y, z, color="r")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
