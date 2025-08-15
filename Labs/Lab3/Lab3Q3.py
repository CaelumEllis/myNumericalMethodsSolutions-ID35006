#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 12:42:43 2025

@author: caelum
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    f = x*np.cos(x) + x*np.sin(x/2)
    return f

a = -10
b = 10
N = 200



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
    
    
    return bracketList
    
def goldSectionSearch(f, listOfBracketPairs):
    GDNR = (1 + np.sqrt(5))/2
    for i in range (0, len(listOfBracketPairs)):
        while np.abs(listOfBracketPairs[i][0] - listOfBracketPairs[i][1]) > 10**-5:
            a = listOfBracketPairs[i][0]
            b = listOfBracketPairs[i][1]
            
            c = b - (b - a)/GDNR
            d = a + (b - a)/GDNR
            
            if f(c) < f(d):
                listOfBracketPairs[i] = (listOfBracketPairs[i][0], d)
            elif f(d) < f(c):
                listOfBracketPairs[i] = (c, listOfBracketPairs[i][1])
        
    return listOfBracketPairs

print(goldSectionSearch(f, minBracket(f, a, b, N)))