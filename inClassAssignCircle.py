#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:09:18 2018

@author: JovaniSenpai
"""

#import all libraries used in equation
import numpy as np

#define function using 'r' for radius for the circle
def makeCircle(r,x0,y0):
    
    thetaVec = np.r_[0:2*np.pi:0.001]
    
    #below is the formula for calcuating points 'x' and 'y' 
    x = r*np.cos(thetaVec) + x0
    y = r*np.sin(thetaVec) + y0
     
    #x and y points of the cirlc will be returned with command 'return'
    return(x,y)
    
    