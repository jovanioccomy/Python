#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:09:18 2018

@author: JovaniSenpai
"""

#import numpy library as 'np'
import numpy as np
#import math library to use 'pi' in this example 
import math

#define function using 'r' for radius and 'h' as height 
def cyl(r, h):
    
    
    #below is the formula for calcuating the area of a cyclinder as variable 'sA'
    sA = 2*math.pi*r*h + 2*math.pi*r**2
    
    #below is the formula for calcuating the volume of a cyclinder as vairable 'V'
    V = math.pi*r**2*h
    
    #values of the surface area and volume will be returned with command 'return'
    return[sA,V]
    
    