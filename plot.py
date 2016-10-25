#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''Plot GPS Satellite Track

Usage:
    plot --prn <prn> --type <type>

Options:
    --prn <prn> PRN number
    --type <type> Plot type

Example:
    plot --prn ' 4' --type 'ECEF'

'''



from cal2gps import cal2gps
import spos
from rinex import readRinexNav
import xyz2neu
import neu2rael
from docopt import docopt

import math
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime


def plot(prn, type='ECEF'):
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

    if type == 'ECEF' or type == 'ECI':
        # Initialization
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')


        # Calculate
        for t in range(518400, 604800, 300):
            [xyz_orbit, i, OMEGA] = spos.orbit(t, t_oe, M_0, Delta_n, sqrt_a, e, omega,
                    Cuc, Cus, Crc, Crs, Cic, Cis, i_0, OMEGA_0, i_dot, OMEGA_DOT)
            [xyz_inertial, OMEGA] = spos.inertial(xyz_orbit, i, OMEGA)
            xyz_ECEF = spos.ecef(xyz_inertial, OMEGA)
            #x_ECEF.append(xyz_ECEF.item(0))
            #y_ECEF.append(xyz_ECEF.item(1))
            #z_ECEF.append(xyz_ECEF.item(2))
            #print([xyz_ECEF.item(0),xyz_ECEF.item(1),xyz_ECEF.item(2)])
            if type == 'ECEF':
                ax.scatter(xyz_ECEF.item(0), xyz_ECEF.item(1), xyz_ECEF.item(2), s=1)

            elif type == 'ECI':
            # Test inertial
                ax.scatter(xyz_inertial.item(0), xyz_inertial.item(1), xyz_inertial.item(2), s=1)
                #plt.axis('equal')


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
    elif type == 'GT':
        fig = plt.figure()
        ax = fig.add_subplot(111)
        map = Basemap(projection='cyl', lon_0=0)
        map.drawcoastlines(color = 'grey')
        map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
        map.drawmeridians(np.arange(map.lonmin, map.lonmax+30, 60),labels=[0,0,0,1])

        #map.drawmapboundary(fill_color='aqua')
        #map.fillcontinents(color='aqua', lake_color='aqua')

        
        for t in range(518400, 604800, 300):
            [xyz_orbit, i, OMEGA] = spos.orbit(t, t_oe, M_0, Delta_n, sqrt_a, e, omega,
                    Cuc, Cus, Crc, Crs, Cic, Cis, i_0, OMEGA_0, i_dot, OMEGA_DOT)
            [xyz_inertial, OMEGA] = spos.inertial(xyz_orbit, i, OMEGA)
            xyz_ECEF = spos.ecef(xyz_inertial, OMEGA)
            [B, L] = spos.groundtrack(xyz_ECEF)
            ax.scatter(L, B, c='red', s=2)



        plt.show()
    elif type == 'POLAR':
        fig = plt.figure()
        ax = fig.add_subplot(111, polar = True)
        
        for t in range(518400, 604800, 300):
            [xyz_orbit, i, OMEGA] = spos.orbit(t, t_oe, M_0, Delta_n, sqrt_a, e, omega,
                    Cuc, Cus, Crc, Crs, Cic, Cis, i_0, OMEGA_0, i_dot, OMEGA_DOT)
            [xyz_inertial, OMEGA] = spos.inertial(xyz_orbit, i, OMEGA)
            xyz_ECEF = spos.ecef(xyz_inertial, OMEGA)
            [N, E, U] = xyz2neu.xyz2neu(xyz_ECEF.item(0), xyz_ECEF.item(1), xyz_ECEF.item(2), 39.9042, -116.9074, 0)
            [R, A, EL] = neu2rael.neu2rael(N, E, U)
            if R > 1:
                ax.scatter(A, R * math.cos(EL), s=1)

        plt.show()
        

def cli():
    arguments = docopt(__doc__)
    prn = arguments.get('--prn')
    t = arguments.get('--type')
    plot(prn, t)

if __name__ == "__main__":
    cli()




