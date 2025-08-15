#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 12:30:33 2025

@author: caelum
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    f = x*np.cos(x) + x*np.sin(x/2)
    return f

a = -5
b = 5
N = 20


def minBracket(f, a, b, N):
    h = (b-a)/N
    x = np.linspace(a, b, N)
    plt.plot(x,f(x))
    plt.show()
    bracketList = []
    for i in range (N-1):
        x = h * i + a 
        if f(x) < f(x-h) and f(x) < f(x+h):
            bracketList.append((x-h, x+h))
    
    print(bracketList)
    return bracketList
    

blist = minBracket(f,a,b,N)

