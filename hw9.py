#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:13:55 2018

@author: JovaniSenpai
"""

import numpy as np


M = np.r_['0,2',[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

#def replaceMat(M):
    
M[0,:]=np.zeros(5)
M[3,:]=np.zeros(5)
M[4,:]=np.zeros(5)
    
    #return M
   
#R = np.r_[1,2,3,4,5]

#Lambda = 1
#x = np.r_[1:100+0.5:0.5]
#E = 1/x*np.exp(-1j*2*np.pi/Lambda*x)