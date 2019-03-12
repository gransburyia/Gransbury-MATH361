# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:50:02 2019

@author: grans
"""

def addTerms(n, a_0):
    terms = []
    terms.append(a_0)
    for ii in range(1,n):
        if(a_0 % 2 == 0):
            a_0 = a_0/2
            terms.append(a_0)
            if(a_0 == 1):
                break
        else:
            a_0 = 3 * a_0 + 1
            terms.append(a_0)
            if(a_0/2 == 1):
                break
    return terms
             
n = 1000

a_0 = 67

termsList = []

for ii in range(1, a_0 + 1):
    termsList.append(addTerms(n, ii))
    print("For the term", ii, "the Collatz terms are",  termsList[ii - 1],".")
    print("This took", len(termsList[ii - 1]), "terms to reach 1.\n")