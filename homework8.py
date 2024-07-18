#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:34:12 2018

@author: JovaniSenpai
"""

#homework 8
#import libraries for numpy and plots
import numpy as np
import matplotlib.pyplot as plt

#function, compute the recieved power given the input
def frissFormula(tPower,tGain,rGain,lamb,r):
    Pr =(tPower*tGain*rGain*(lamb**2)) / (4*np.pi*r)**2
    return Pr

#set variables
#transmit power
tPower = 10 #watts
#transmit gain
tGain = 1.5
#recieve gain
rGain = 1

#the speed of light
c = 3e8 #m/s

#stepsize
freqVec = np.r_[800e6:1900e6:10e6]

#the matching wavelength vector
lamb = c/freqVec
rVec = np.r_[5e3,10e3,30e3] #km

#create a matrix to hold results
mat = np.zeros([len(rVec),len(freqVec)]) 
for ii, r in enumerate(rVec):
    mat[ii,:]= frissFormula(tPower,tGain,rGain,lamb,r)

#plot all data, note: 1e6 is sci. notation 
plt.figure()
#plot 
plt.plot(freqVec/1e6,10*np.log10(mat[0,:]), color = 'g', linewidth = 3)
#plot 
plt.plot(freqVec/1e6,10*np.log10(mat[1,:]), color = 'c',  linewidth = 3)
#plot 
plt.plot(freqVec/1e6,10*np.log10(mat[2,:]), color = 'y', linewidth = 3) 
#xlabel 
plt.xlabel('Frequency (Mhz)')
#ylabel
plt.ylabel('Recieved Power (dB)')
plt.show()

#part two
#set variables
#transmit power
tPower = 1 #watt
#transmit gain
tGain = 1
#recieve gain
rGain = 1.5

#create a matrix to hold results
matii = np.zeros([len(rVec),len(freqVec)]) 
for iii, r in enumerate(rVec):
    matii[iii,:]= frissFormula(tPower,tGain,rGain,lamb,r)

#plot all data, note: 1e6 is sci. notation 
plt.figure()
#plot 
plt.plot(freqVec/1e6,10*np.log10(matii[0,:]), color = 'b', linewidth=3)
#plot 
plt.plot(freqVec/1e6,10*np.log10(matii[1,:]), color = 'm', linewidth=3) 
#plot 
plt.plot(freqVec/1e6,10*np.log10(matii[2,:]), color = 'g', linewidth=3) 
#xlabel 
plt.xlabel('Frequency (Mhz)')
#ylabel
plt.ylabel('Recieved Power (dB)')
plt.show()