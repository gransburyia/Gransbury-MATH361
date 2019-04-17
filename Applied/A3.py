# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:26:20 2019

@author: grans
"""

import numpy as np

def ltgDividesltr(x, y):
    if x >= y:
        return True
    else:
        return False
    
def rempty():
    if r_array[0][0] == 0 and r_array[0][0] == 0:
        return True
    else:
        return False
    
def dividingTerms(x, y): #input will be r_array[0] and g_array[0]
    coef = x[0][0] / y[0][0]
    power = x[0][1] - y[0][1]
    return np.array([coef, power])

def mulTermsByG(array):
    h = np.array([0,0])
    for i in range(0, len(g_array)):
        power = array[0][1]
        hpower = g_array[i][1] + power
        coef = array[0][0]
        hcoef = g_array[i][1] * coef
        h = np.vstack([h, np.array([hcoef, hpower])])
        return h
        
#def addingTerms(array):
        
#def subTerms():
        
def makeNegative(array):
    for i in range(0, len(array)):
        array[i][0] = -1 * array[i][0]


            
    

g_array = np.array([[1,1],[2,0],[0,0]])

f_array = np.array([[1,3],[-1,0]])

q_array = np.array([0,0])

r_array = f_array

while rempty() == False and ltgDividesltr == True:
    #q += dividingTerms(r_array[0], g_array[0])
    #r -= mulTermsByG(dividingTerms(r_array[0], g_array[0]))
    


