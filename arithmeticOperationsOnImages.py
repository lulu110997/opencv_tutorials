#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('/home/louis/opencvTutorial/babyYoda.png',1)
img1 = cv2.resize(im, (180,222)) # Resize image to be the same as the img2
img2 = cv2.imread('/home/louis/opencvTutorial/opencv_logo.png',1)

# You can add two images by OpenCV function, 
# cv2.add() or simply by numpy operation, 
# res = img1 + img2. Both images should be of 
# same depth and type, or second image can 
# just be a scalar value.

# OpenCV addition is a saturated operation 
# while Numpy addition is a modulo operation
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y)) # 250+10 = 260 => 255. Preferred method
print(x+y) # 250+10 = 260 % 256 = 4

imagesAdded = cv2.add(img1,img2)
cv2.imshow('addedImages',imagesAdded) # Note  how adding two images together changes the pixel color intensity
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image blending for transparent effects
# Check that the two images are the same size
print(img2.shape)
print(img1.shape) 
# The two images are blendedFirst image is given 
# a weight of 0.7 and second image is given 0.3 
dst = cv2.addWeighted(img1,0.9,img2,0.2,-1)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise operation. They will be highly useful 
# while extracting any part of the image
# Below is an example on how to change a
# particular region of an image
img1 = cv2.resize(im, (960,540)) # Resize image for the next example

# To put the logo on top-left corner, create an ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]


# Now create a mask of logo and create its inverse mask also
# 'masking' refers to the practice of using a mask to protect a specific area of an image
# Masking an area of an image protects that area from being altered by changes made to the rest of the image
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # Threshold method requires src image to be a grayscale image
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask) # Invserse the grayscale image

# Now black-out the area of logo in ROI. Mask out stuff from the roi using mask_inv
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('final',img1)
cv2.imshow("img2gray", img2gray)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('mask',mask)
cv2.imshow("img1_bg", img1_bg)
cv2.imshow("img2_fg", img2_fg)
cv2.imshow("dst", dst)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
