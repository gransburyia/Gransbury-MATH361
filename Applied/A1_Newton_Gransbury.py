# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:07:04 2019

@author: grans
"""

import numpy as np

n = 250 #represents the max number of iterations
TOL = 1 * 10 ** (-4) #represent the tolerance at which we will stop the iterative process
z_0 = 2 #initial iterate of Newton's Method
z_1 = 0

x = lambda x: (1/100) * ((x ** 4) + ((np.e - 2 - np.sqrt(2)) * x ** 3) + ((2 * np.sqrt(2) - np.sqrt(2 * np.e) - 3 - 2 * np.e) * x ** 2) + ((2 * np.sqrt(2 * np.e) + 3 * np.sqrt(2) - 3 * np.e) * x) + 3 * np.sqrt(2 * np.e))
dx = lambda x: (1/100) * (4 * x ** 3) + (3 * (np.e - 2 - np.sqrt(2)) * x ** 2) + (2 * (2 * np.sqrt(2) - np.sqrt(2 * np.e) - 3 - 2 * np.e) * x) + (2 * np.sqrt(2 * np.e) + 3 * np.sqrt(2) - 3 * np.e)
i = 0;
tol = 0;

calcs = np.array([0, 0, 0])

calcs = np.vstack([calcs, np.array([0, z_0,0])])

while i < n or tol >= TOL:
    z_1 = z_0 - (x(z_0)/dx(z_0))
    tol = abs(z_1 - z_0)
    i += 1
    calcs = np.vstack([calcs, np.array([i, z_1, tol])])
    z_0 = z_1
    
    
print("This is the final value:", z_1)
print("These are all values before and the tols:\n", calcs[1:][:])