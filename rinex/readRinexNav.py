# -*- coding: utf-8 -*-
"""
Reads RINEX 2 Navigation files
xcalcor@gmail.com
MIT License
"""

import numpy as np
from pathlib2 import Path
from datetime import datetime
from pandas import DataFrame
from io import BytesIO

def readRinexNav(file_nav, prn=' 4'):
    """
    http://gage14.upc.es/gLAB/HTML/GPS_Navigation_Rinex_v2.11.html
    """

    file_nav = Path(file_nav).expanduser()
    
    startcol = 3 # column where numerical data starts
    nfloat = 19 # number of text elements per float data number
    nline = 7 # number of lines per record

    with file_nav.open('r') as f:
        while True:
            if 'END OF HEADER' in f.readline(): break

        sv = []; epoch = []; raws = ''
        while True:
            headln = f.readline()
            if not headln: break
            # Header
            if prn not in headln[:2]: continue
            #print(headln[:2])
            #print('True' if prn in headln[:2] else 'False')
            sv.append(headln[:2])
            year = int(headln[2:5])
            if 80 <= year <= 99:
                year += 1900
            elif year < 80:
                year += 2000
            
            epoch.append(datetime(year = year,
                                  month         = int(headln[5:8]),
                                  day           = int(headln[8:11]),
                                  hour          = int(headln[11:14]),
                                  minute        = int(headln[14:17]),
                                  second        = int(headln[17:20]),
                                  microsecond   = int(headln[21])*100000))

    # Get data
            raw = (headln[22:].rstrip() +
                    ''.join(f.readline()[startcol:].rstrip() for _ in range(nline)))
            raws = raws + raw + '\n'

    raws = raws.replace('D','E')

    b_str = BytesIO(raws.encode())
    # Get string from bytesIO
    data = np.genfromtxt(b_str, delimiter = nfloat)
    
    nav = DataFrame(np.hstack((np.asarray(sv, int)[:, None], data)), epoch,
                ['sv', 'SVclockBias', 'SVclockDrift', 'SVclockDriftRate', 'IODE',
                'Crs', 'DeltaN', 'M0', 'Cuc', 'Eccentricity', 'Cus', 'sqrtA', 'TimeEph',
                'Cic', 'OMEGA', 'Cis', 'Io', 'Crc', 'omega', 'OMEGA DOT', 'IDOT',
                'CodesL2', 'GPSWeek', 'L2Pflag', 'SVacc', 'SVhealth', 'TGD', 'IODC',
                'TransTime', 'FitIntvl', 'empty1', 'empty2'])

    return nav



