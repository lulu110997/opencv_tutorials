#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

# In this tutorial, you will learn how to convert images from one color-space to another, 
# like BGR <->  Gray, BGR <-> HSV etc

# For color conversion, we use the function 
# cv2.cvtColor(input_image, flag) where flag 
# determines the type of conversion.

# For BGR <-> Gray conversion we use the flags 
# cv2.COLOR_BGR2GRAY. Similarly for BGR <-> HSV, 
# we use the flag cv2.COLOR_BGR2HSV.

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags) # Prints out all the flags available

# For HSV, Hue range is [0,179], Saturation range 
# is [0,255] and Value range is [0,255]. Different 
# ftwares use different scales. So if you are 
# comparing OpenCV values with them, you need to 
# normalize these ranges

cap = cv2.VideoCapture(4)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV. Easier to represent color in this space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Masks two colours https://stackoverflow.com/questions/48109650/how-to-detect-two-different-colors-using-cv2-inrange-in-python-opencv
    # define range of red color in HSV
    lower_red = np.array([160,20,70])
    upper_red = np.array([190,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image. You want to place a new 'frame' in 'frame' by masking out 'mask'
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

# To find HSV values to track. Use green as example (can be applied for any BGR)
# green = np.uint8([[[0,255,0 ]]])
# hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# print hsv_green
# Now you take [H-10, 100,100] and 
# [H+10, 255, 255] as lower bound 
# and upper bound respectively