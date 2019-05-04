# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:41:46 2019

@author: grans
"""
from PIL import Image as im

def putValue(x, y, z0):
    for k in range(n):
        z1 = z0 - f(z0) / d(z0) #newton's method
        if abs(z1 - z0) < TOL: # stop when close enough to any root
            break
        z0 = z1 #sets initial guess to number just calculated.
    #puts the value of the 3-tuple(a color) in the tuple (i,j) in the image
    image.putpixel((x, y), (k % 16 * 16, k % 8 * 32, k % 4 * 64))

imgx = 512 #length of the x "axis"
imgy = 512 #length of the y "axis"

image = im.new("RGB", (imgx, imgy)) #mode of RGB and size of 512 pixels by 512 pixels

#length of the axes
bottom = -1.0
top = 1.0
left = -1.0
right = 1.0

n = 200 # max iterations allowed
TOL = 1e-4 #represent the tolerance at which we will stop the iterative process

f = lambda x: x ** 3 - 1 #original function
d = lambda x: 3 * x ** 2 #derivative of that function

# the first two loops determing a numerical value that corresponds to a pixel in the image
for i in range(imgy): 
    y = i * (right - left) / (imgy - 1) + left
    for j in range(imgx):
        x = j * (top - bottom) / (imgx - 1) + bottom
        #uses the complex number of the pixel in the 512X512 image and uses that as the intial guess
        z0 = complex(x, y)
        #This function uses newtons method to find the root that the initial guess goes too and puts 
        #the color corresponding to a root in a pixel at the position found in the 2 for loops before
        putValue(i, j, z0)

#saves the image as a png under the name you wish to name the file.
image.save("fractal.png", "PNG")