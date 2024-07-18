#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:27:12 2018

@author: JovaniSenpai
"""
import numpy as np
import matplotlib.pyplot as plt

numstamp = 2000; 
e0 = 1
Oc = 0
Oa = 0
fC = 15
fA = 2
a = 0.5
t = np.linspace(0,1,numstamp) 

eCt = e0*np.cos(2*np.pi*fC*t + Oc)
xT = a*np.sin(2*np.pi*fA*t + Oa)
eT = eCt*(1 -(a/2 ))*(1-(xT/a))

  
#plot all data on a single figure
plt.figure()
plt.plot(t,eCt)
plt.plot(t,xT)
plt.plot(t,eT)
plt.legend(['carrier','dt','total'])
plt.xlabel('time(s)',frontsize = 14, fontweight = 'bold')
plt.ylabel('signal',fontsize = 14, fontweight = 'bold')
plt.grid()
plt.gca.tick_params(axis='both',labelsize=14)

#for loop
f = [1,2,3,4] 
plt.figure()
for y in range(4):
    xT1 = a*np.sin(2*np.pi*f[y]*t + Oa)
    eT1 = eCt*(1- a/2*(1-xT1/a))
    plt.plot(t,eT1)
plt.xlabel('time(s)',frontsize = 14, fontweight = 'bold')
plt.ylabel('amplitude',fontsize = 14, fontweight = 'bold')
plt.gca.tick_params(axis='both',labelsize=14)
plt.legend(['1','2','3','4'])
plt.grid()   
    
    

 
