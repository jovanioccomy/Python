#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:24:12 2018

@author: JovaniSenpai
"""

#import numpy library for multipliction functions, etc and mtlplotlib.pyplot in order to plot figures
import numpy as np
import matplotlib.pyplot as plt

#Create a histogram that shows a bell curve that is centered around 100 with a standard deviation of 15
mu, sigma = 100, 15

#variable x will calculate mu, sigm times a random number up to 10000
x = mu + sigma*np.random.randn(10000)

#plot the formula for variable x 
plt.figure()
plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

#x, y labels
plt.xlabel('Smarts')
plt.ylabel('Probability')

#x, y limits
plt.xlim(40, 160)
plt.ylim(0,0.03)

#plt.grid turns the grid on or off
plt.grid()

#plt.title names the graph, it will be named 'Histogram of IQ'
plt.title('Histogram of IQ')