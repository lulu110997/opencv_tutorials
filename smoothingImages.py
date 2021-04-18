#!/usr/bin/env python2

import cv2
import numpy as np 
from matplotlib import pyplot as plt

# A LPF helps in removing noise, or blurring the image. 
# A HPF filters helps in finding edges in an image.

img = cv2.imread('opencv_logo.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

# Image blurring is achieved by convolving the image 
# with a low-pass filter kernel. It is useful for 
# removing noise. It actually removes high frequency 
# content (e.g: noise, edges) from the image resulting 
# in edges being blurred when this is filter is applied

# Averaging  simply takes the average of all the pixels under kernel area and replaces the central element with this average
# Gaussian filtering is highly effective in removing Gaussian noise from the image
# This is highly effective in removing salt-and-pepper noise
# Bilateral filtering. Filter of choice when edges in the image needs to be preserved
img = cv2.imread('opencv_logo.png')

# blur = cv2.blur(img,(10,10)) #Averaging cv2.boxFilter() can also be used
# blur = cv2.GaussianBlur(img,(5,5),0)
# median = cv2.medianBlur(img,5) # Median blur
blur = cv2.bilateralFilter(img,9,75,75) # bilateral filtering
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()