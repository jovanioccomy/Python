#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:17:43 2018

@author: JovaniSenpai
"""
#import libraries for numpy, circle, and plots
import numpy as np
import circle as cir
import matplotlib.pyplot as plt

radiiVec = [3,5,7,10,13]

#set variables
x0 = 3
y0 = 3

#delcare a plot
plt.figure()
# calculate all valueswith a for loop
for radius in radiiVec:

    (x,y) = cir.makeCircle(radius,x0,y0)

plt.plot(x,y)

plt.xlabel('x axis')
plt.ylabel('y axis')