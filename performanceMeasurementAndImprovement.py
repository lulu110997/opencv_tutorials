#!/usr/bin/env python2
import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('/home/louis/opencvTutorial/babyYoda.png',1)
img1 = cv2.resize(im, (960,540)) # Resize image to fit in screen

# Similar to tic toc function of MATLAB
e1 = cv2.getTickCount() # returns the number of clock-cycles after a reference event 
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/ cv2.getTickFrequency()
print(t)

cv2.useOptimized() # Should return TRUE if not, run cv2.setUseOptimized(True)

# Normally, OpenCV functions are faster than Numpy 
# functions. So for same operation, OpenCV 
# functions are preferred. But, there can be 
# exceptions, especially when Numpy works with 
# views instead of copies.






###################################

# img = cv2.imread('/home/louis/opencvTutorial/babyYoda.png',1)
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)

# img=cv2.drawKeypoints(gray,kp)

# cv2.imwrite('sift_keypoints.jpg',img)