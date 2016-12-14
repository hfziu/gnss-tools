# -*- coding: utf-8 -*-
"""
Satellite Parameters
xcalcor@gmail.com

Test:
    spos.spos(181139.924058, 180000, -0.102819239085e1, 0.382373066543e-8, 0.515372436142e4, 0.659382948652e-2, -0.178159728487e1, 0.165402889252e-5, 0.764429569244e-5, 0.24821875e3, 0.323125e2, -0.372529029846e-7, 0.106170773506e-6, 0.989287064691, -0.563362973163, 0.832177521337e-10, -0.789782905741e-8)

The result should be:
    matrix([[-14698515.69787471],
            [ 19392222.95870894],
            [-10362247.69996771]])
"""

import math
import numpy as np
import rotate

import xyz2blh

def orbit(t, t_oe, M_0, Delta_n, sqrt_a, e, omega, Cuc, Cus, Crc, Crs, Cic, Cis, i_0, OMEGA_0, i_dot, OMEGA_DOT):
    # 平均角速度
    mu = 3.986005e14
    n_0 = sqrt_a ** -3 * math.sqrt(mu)
    n = n_0 + Delta_n

    # 
    t_k = t - t_oe
    if t_k > 302400:
        t_k = t_k - 604800
    elif t_k < -302400:
        t_k = t_k + 604800

    # 
    M = M_0 + n * t_k

    # Calculate E
    E = M
    E_iter = M + e * math.sin(E)
    while abs(E - E_iter) > 1e-13:
        E = E_iter
        E_iter = M + e * math.sin(E)
    E = E_iter

    # Calculate r_0
    r_0 = sqrt_a ** 2 * (1 - e * math.cos(E))

    # Calculate f
    tan_fd2 = (math.sqrt(1 + e)) / (math.sqrt(1 - e)) * math.tan(E / 2)
    f = math.atan(tan_fd2) * 2

    #  Calculate Phi_k
    Phi_k = omega + f

    # Calculate delta_u, delta_r, delta_i
    delta_u = Cuc * math.cos(2 * Phi_k) + Cus * math.sin(2 * Phi_k)
    delta_r = Crc * math.cos(2 * Phi_k) + Crs * math.sin(2 * Phi_k)
    delta_i = Cic * math.cos(2 * Phi_k) + Cis * math.sin(2 * Phi_k)

    # Calculate u, r, i
    u = Phi_k + delta_u
    r = r_0 + delta_r
    i = i_0 + i_dot * t_k + delta_i
    
    # Calculate OMEGA
    omega_e = 7.2921151467e-5
    OMEGA = OMEGA_0 + (OMEGA_DOT - omega_e) * t_k - omega_e * t_oe

    # SatPos
    x_sat = r * math.cos(u)
    y_sat = r * math.sin(u)
    z_sat = 0

    sat_pos = np.mat([[x_sat],[y_sat],[z_sat]])

    # wgs_84_pos = np.dot(np.dot(rotate.R3(-1*OMEGA),rotate.R1(-1*i)),sat_pos)

    return [sat_pos, i, OMEGA]
    
def inertial(sat_pos, i, OMEGA):
    inertial_pos = np.dot(rotate.R1(-1*i),sat_pos)

    return [inertial_pos, OMEGA]

def ecef(inertial_pos, OMEGA):
    wgs_84_pos = np.dot(rotate.R3(-1*OMEGA),inertial_pos)
    return wgs_84_pos

def groundtrack(wgs_84_pos):
    [B, L, H] = xyz2blh.xyz2blh(wgs_84_pos.item(0), wgs_84_pos.item(1), wgs_84_pos.item(2))
    return [B, L]


