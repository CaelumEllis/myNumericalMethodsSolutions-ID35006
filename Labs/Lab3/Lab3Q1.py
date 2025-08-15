#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 11:12:15 2025

@author: caelum
"""

import numpy as np
import matplotlib.pyplot as plt

N = 200
x = np.linspace(-10, 10, N)

def f(x):
    return x*np.cos(x) + x*np.sin(x/2)

# plt.plot(x,f(x))
# plt.show()

def minBracket(a, b, N):
    h = (b-a)/N
    bracketList = []
    for i in range (N-1):
        x = h * i - 10 
        if f(x) < f(x-h) and f(x) < f(x+h):
            bracketList.append((x-h, x+h))
            
    return bracketList

print(minBracket(-10,10,N))




