#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:49:37 2018

@author: wei
"""

from __future__ import  division
import numpy as np
from matplotlib import pyplot as plt

from rs import RejectionSampling

def l(x):
    return pow(-np.log(x), 2) * pow(x, 2) * (1.0-x)
    
def h(x):
    return 3*pow(x ,2) - 2 * pow(x, 3)

def f(x):
    return pow(-np.log(x), 2) * pow(x, 3) * pow(1.0-x, 2)

RS = RejectionSampling(l, h, 0.1)
N = 1000
g = np.zeros(N)
conv = np.zeros(N)
for i in range(N):
    x = RS.draw()
    g[i] = pow(1-x, 0.5)* 919.0 / 108000
    conv[i] = np.mean(g[:i+1])
    
print(g.mean(), g.var())
plt.plot(range(1, N+1), conv)
plt.title('Convergence of MC Integration')
plt.xlabel('Number of Samples')
plt.ylabel(r'$I_N$')
plt.show()

Var = (sum(g**2)/N - g.mean()**2)/N
print(Var)