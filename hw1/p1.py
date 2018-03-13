#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:11:09 2018

@author: wei
"""
from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt


def l(x):
    return (-np.log(x))**2 * x**2 * (1.0-x)/6

def h(x):
    return 3*pow(x ,2) - 2 * pow(x, 3)

def binarySearch(u):
    lo = 0.0
    hi = 1.0
    while (hi - lo) > 1e-15:
        
        mid = lo + (hi - lo) / 2
        if h(mid) < u:
            lo = mid
        elif h(mid) > u:
            hi = mid
        else:
            return mid
    return mid

def draw():
    u = np.random.rand()
    x = binarySearch(u)
    return x
    
n = 1000000 # number of samples
M = 1.0/60  # bound (not sharp) of l(x)
sample = np.zeros(n)
accept = 0
reject = 0

while accept < n:
    u = np.random.rand()
    x = draw()
    if u < l(x) / M:
        sample[accept] = x
        accept += 1
    else:
        reject += 1
        
plt.figure()
plt.hist(sample, bins=100, normed = True)
plt.show()
plt.title('Sample from f(x)')

print(accept / (accept+reject))