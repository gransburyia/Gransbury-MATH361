# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:10:17 2019

@author: grans
"""
import numpy as np


def findingTriples(x, n):
    for ii in range(1,n):
        for jj in range(ii,n):
            c = (ii**2) + (jj**2)
            c_root = int(np.sqrt(c))
            if (ii < jj) and (jj < c_root) and (c == (c_root ** 2)):
                x = np.vstack( [ x,np.array([ii,jj,c_root]) ] )  
            if (ii < jj) and (jj < c_root) and (c == (c_root ** 2) and (ii + jj + c_root == 1026)):
                print(ii,"+",jj,"+",c_root,"= 1026")           
    print(x)
                
x = np.zeros([0,3])

n = 350

findingTriples(x, n)



