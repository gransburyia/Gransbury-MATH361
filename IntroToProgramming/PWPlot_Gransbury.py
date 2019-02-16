# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:35:29 2019

@author: grans
"""

import numpy as np
import matplotlib.pyplot as plt

def functions():
    for ii in x:
        if ii < 2:
            values.append(-3*(ii + 2)**2 + 1)
        elif ii >= -2 and ii < -1:
            values.append(1)
        elif ii >= -1 and ii <= 1:
            values.append((ii-1)**3 + 3)
        elif ii > 1 and ii < 2:
            values.append(np.sin(np.pi*ii) + 3)
        elif ii >= 2:
            values.append(3 * np.sqrt(ii - 2) + 4)
        
        
values = []   

n = 1000

x = np.linspace(-3, 3, n) 

functions()

plt.plot(x,values)    
plt.show()