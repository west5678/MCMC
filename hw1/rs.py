#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:44:35 2018

@author: wei
"""

import numpy as np

class RejectionSampling():
    def __init__(self, l, H, M):
        self.l = l
        self.h = H
        self.M = M
    
    def binarySearch(self, u):
        lo = 0.0
        hi = 1.0
        while (hi - lo) > 1e-15:
            
            mid = lo + (hi - lo) / 2
            if self.h(mid) < u:
                lo = mid
            elif self.h(mid) > u:
                hi = mid
            else:
                return mid
        return mid
    
    def drawFromH(self):
        u = np.random.rand()
        x = self.binarySearch(u)
        return x
    
    def draw(self):
        while True:
            u = np.random.rand()
            x = self.drawFromH()
            if u < self.l(x) / self.M:
                return x

