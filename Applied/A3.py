# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:26:20 2019

@author: grans
"""

import numpy as np
#Erase high degree terms that are now zero
# Assumed that highest degree of p is last element of list
def clean_poly():
    highest_deg = len(r_list) - 1   
    for ii in range(len(r_list)-1,-1,-1):
        if np.abs(r_list[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
    del r_list[highest_deg+1:]

def rempty(): #checks if r = 0
    for i in r_list:
        if i != 0:
            return False
    return True

def ltgDividesltr(): #input will be degrees for the first terms
    if len(r_list) >= len(g_list):
        return True
    else:
        return False
    
def calculatingQ():
    #adds ltr/ltg to q
    if len(r_list) == len(g_list):
        q_list.insert(0, r_list[-1]/g_list[-1])
    else:
        #adds 0 to the list of missing place values
        for i in range(0, len(r_list) - len(g_list) -1):
            q_list.insert(i, 0)
        q_list.insert(len(r_list) - len(g_list), r_list[-1]/g_list[-1])
        
def calculatingR():
    #gets ltr/ltg
    temp_r = [0]
    if len(r_list) == len(g_list):
        temp_r.insert(0, r_list[-1]/g_list[-1])
    else:
        for i in range(0, len(r_list) - len(g_list) -1):
            temp_r.insert(i, 0)
        temp_r.insert(len(r_list) - len(g_list), r_list[-1]/g_list[-1])
    #multiplies ltr/ltg by g and multiplies by -1
    temp_g = list(g_list)
    for i in range(0,len(temp_g)):
        temp_g[i] = (temp_g[i] * temp_r[-1]) * -1
    for i in range(0,len(temp_r)-1):
        temp_g.insert(0,0)
    #adds g to r
    for i in range(0,len(g_list)):
        r_list[i] = r_list[i] + temp_g[i]
    clean_poly()

    
"""
main
"""
            
g_list = [2, 1]

f_list = [-1, 0, 0, 1]

q_list = [0]

r_list = list(f_list)

while rempty() == False and ltgDividesltr() == True:
    calculatingQ()
    calculatingR()




