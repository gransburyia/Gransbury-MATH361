# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:23:30 2019

@author: grans
"""

import numpy as np

def primeCheck(n):
    trueOrFalse = False
    if(n == 2):
        return True
    elif(n > 1):
        for ii in range(2,n):
            if(n % ii == 0):
                trueOrFalse = False
                break
            else:
                trueOrFalse = True
    return trueOrFalse

def func(n):
    for ii in range(9, n, 2):
        if(primeCheck(ii) == False):
            test = False
            for jj in range(1, int(np.sqrt(ii))):
                difference = ii - (2 * (jj ** 2))
                if(difference > 0):
                    if((primeCheck(difference) == True) or difference == 1):
                        test = True;
        if(test == False):
              return ii
print("The number that breaks goldbach's conjecture is",func(6000), ".")
         