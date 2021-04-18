#!/usr/bin/env python2

import cv2
import numpy as np 
from matplotlib import pyplot as plt

# Morphological transformations are some simple operations 
# based on the image shape. It is normally performed on 
# binary images. It needs two inputs, one is our original 
# image, second one is called structuring element or kernel 
# which decides the nature of operation

# Erosion: erodes away the boundaries of foreground object (Always try to keep foreground in white)
# It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects 
img = cv2.imread('j.png',0)
kernel = np.ones((10,10),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 3)
cv2.imshow('img1', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Dilation: opposite of erosion. Useful in joining broken parts of an object
dilation = cv2.dilate(erosion,kernel,iterations = 3)
cv2.imshow('img2', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Other morphological transormations
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # erosion followed by dilation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # dilation followed by erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) # difference between dilation and erosion of an image (will return the outline of the image)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) # difference between input image and opening of the image
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel) # difference between the closing of the input image and input image

# Obtaining different shaped kernels
cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # for a rectangular kernel
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) # for an elliptical circle
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) # for a cross shape circle