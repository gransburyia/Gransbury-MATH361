# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:29:28 2019

@author: grans
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt

stopNum = int(input("Enter a number that corresponds to the total number of terms in the partial sum sequence: \n"))

products= np.zeros([3,stopNum])

productToI = 1.0

for jj in range(1,stopNum+1):
    productToI *= (jj**3)-1/(jj**3)+1
    products[0][jj-1] = productToI
   
productToI = 1.0 
for jj in range(1,stopNum+1):
    productToI *= float(m.exp(jj/100))/ float(jj**10)
    products[1][jj-1] = productToI
    
productToI = 1.0
for jj in range(1,stopNum+1):
    productToI *= (jj**2 + m.factorial(jj)) / m.factorial(jj-1)
    products[2][jj-1] = productToI
          
print("The first partial products are:")
print("The first 15 are:")
print(products[0][:15])
print("The last 15 are:") 
print(products[0][-15:])

listx=[]
for ii in range(1, stopNum + 1):
    listx.append(ii)

x =listx
y =products[0][:]



plt.plot(x,y)
plt.show()

print("The second partial products are:")
print("The first 15 are:")
print(products[1][:15])
print("The last 15 are:") 
print(products[1][-15:])

x =listx
y =products[1][:]


plt.plot(x,y)
plt.show()

print("The third partial products are:")
print("The first 15 are:")
print(products[2][:15])
print("The last 15 are:") 
print(products[2][-15:])

x =listx
y =products[2][:]

plt.plot(x,y)
plt.show()