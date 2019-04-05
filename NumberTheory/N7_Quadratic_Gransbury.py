# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:50:35 2019

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

p = 50

count = np.array([0,0])
neg_one = np.array([0,"True"])

for i in range(2,p+1):
    if primeCheck(i) == True:
        residues = []
        countRes = 0
        for j in range(0, i):
            number = (j * j) % i
            residues.append(number)
        if residues.count(i-1) > 0:
            neg_one = np.vstack( [neg_one, np.array([i,"True"])] )
        else:
            neg_one = np.vstack([neg_one, np.array([i,"False"])])
            
        residues = set(residues)
        countRes = len(residues)
            
        count = np.vstack( [count, np.array([i,countRes])] )

for i in range(1, len(count)):
    print("This is the amount of residues of Z mod", count[i][0]," is:", count[i][1])
    print("-1 is a residue of Z mod", neg_one[i][0],"is:", neg_one[i][1])
        
    
