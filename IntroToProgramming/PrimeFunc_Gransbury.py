# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:42:29 2019

@author: grans
"""

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
    


n = 8

print(primeCheck(n))

prime = []

testNum = 2

while(len(prime) <n):
    if(primeCheck(testNum) == True):
        prime.append(testNum)
        testNum += 1
    else:
        testNum += 1
    
print("The", n,"th prime number is", prime[n - 1],".")