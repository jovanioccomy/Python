#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 09:14:48 2018

@author: JovaniSenpai
"""

#Homework 6: Jovani Occomy

#import numpy as variable np
import numpy as np

import matplotlib.pyplot as plt


#set variables

#variable 'lamb' (lambda) 

lamb = 1.5 # units are in meters

 
#variable 'x' is wavelength lambda ('lamb') over 40

x = np.arange(0,4*lamb,lamb/40)

 

#set all 4 SNR variables 

SNR1 = 5 #units are in db

SNR2 = 10 #units are in db

SNR3 = 20 #units are in db

SNR4 = 30 #units are in db

 

 

#varibale 'E' calculates an electromagnetic plane wave traveling in the air using SNR1 - 4's data

E1 = 10**(SNR1/20)*np.exp(-1j*2*np.pi/lamb*x)

E2 = 10**(SNR2/20)*np.exp(-1j*2*np.pi/lamb*x)

E3 = 10**(SNR3/20)*np.exp(-1j*2*np.pi/lamb*x)

E4 = 10**(SNR4/20)*np.exp(-1j*2*np.pi/lamb*x)

 

#variable 'N' calculates the noise in a signal-to-noise ratio 

N = 1/(np.sqrt(2))*(np.random.randn(np.size(E1))+1j+np.random.randn(np.size(E1))) #units re in db


# variable 'Y' calculates the recived signals with noise

Y1 = E1 + N

Y2 = E2 + N

Y3 = E3 + N

Y4 = E4 + N

 

#plot data on seperate figures

plt.figure()
#Y1
plt.plot(x,np.real(Y1))
#Y2
plt.plot(x,np.real(Y2))
#Y3
plt.plot(x,np.real(Y3))
#Y4
plt.plot(x,np.real(Y4))