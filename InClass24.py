#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:38:22 2018

@author: JovaniSenpai
"""

#import the libraries to execute problems 
import numpy as np
import matplotlib.pyplot as plt

#Create dummy data with variable 'M'  
M = np.random.random_integers(0,100,(7,7))

#Create file for ID writing
fid = open('mycsv.csv','wb')

np.savetxt(fid, M, delimiter=',',fmt='%i %i %i %i %i %i %i')

fid.close()

#Open the file
fid = open('mycsv.csv')

#result variable 
result = np.genfromtxt(fid,delimiter=' ')

fid.close()

#plot the results via rows
thirdRow = result[2,:]
fifthRow = result[4,:]

plt.figure()
plt.plot(thirdRow)
plt.plot(fifthRow**2)
plt.xlabel('index number')
plt.ylabel('numerical value')