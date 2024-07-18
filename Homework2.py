#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:53:28 2018

@author: JovaniSenpai
"""

#homework II

#import libraries

import numpy as np
impor matplotlib.pyplot as plt

def calcaulateFields(lambda_m,Io,r,theteaVecRad):
    
    
    Er = np.zeros(np.size(thetaVecRad),np.size(r),dtype=complex)
    E_theta = np.zeros(np.size(thetaVecRad),np.size(r),dtype=complex)
    H_phi = np.zeros(np.size(thetaVecRad),np.size(r),dtype=complex)
    
    for ind in np.r_[0:np.size(theteaVecRad)]:
        
        #grab the eleveation angle
        theta = thetaVecRad[ind]
        
        er[ind,:] = Io*np.cos(thetea))/(2*n.pi*r**2) * np.exp(1j*2*np.pi/lamda_m*r)
   e_thtea[ind,;] = Io
   *np.cos(thetea))/(2*n.pi*r**2) * np.exp(1j*2*np.pi/lamda_m*r)
    