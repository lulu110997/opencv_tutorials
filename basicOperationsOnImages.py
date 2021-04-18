#!/usr/bin/env python2

import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('/home/louis/opencvTutorial/babyYoda.png',1)
img = cv2.resize(im, (960,540)) # Resize image to fit in screen

# You can access a pixel value by its row and column 
# coordinates. For BGR image, it returns an array of 
# Blue, Green, Red values. For grayscale image, just 
# corresponding intensity is returned.
px = img[100,100] # Access the pixel by its row and column
print("BGR value is,", px) # prints the pixel colour/intensity values
blue = img[100,100,0] # Access only the blue pixel
print("blue intensity is,", blue)

img[100,100] = [255, 255, 255] # Modify the pixel value of the image
print("pixel [100 100[ intensity is", img[100,100])

# For individual pixel access
print("red intensity is", img.item(100,100,2))
# Change red intensity of pixel [100 100]
img.itemset((100,100,2), 100)
print("new red intensity is",img.item(100,100,2))

# Returns a tuple of number of rows, columns and 
# channels (if image is color)
# If image is grayscale, tuple returned contains 
# only number of rows and columns
print (img.shape) 
print("number of pixel is", img.size) # Access total number of pixel
print("image type is", img.dtype) # Access image datatype

ball = img[280:340, 330:390] # Access a region in the image
img[273:333, 100:160] = ball # Replace that region in the image with something else

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split and merge the BGR channels of an image
# Note that indexing is much faster so this method
# should only be used when necessary
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

b = img[:,:,0] # Sets all the blue intensity to 0 using the split method
img[:,:,2] = 50 # Sets all the blue intensity to 50 using numpy indexing. Preffered method

# Making borders for images (Padding)
#  (Image is displayed with matplotlib. So RED and BLUE planes will be interchanged)
# cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
BLUE = [255,0,0]

img1 = cv2.imread('/home/louis/opencvTutorial/opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE) # Last element is replicated throughout
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT) # Border will be mirror reflection of the border element
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101) # Same as above, but with a slight change
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP) # Not sure. Check what it looks like
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE) # Adds a constant colored border. The value should be given as next argument.

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()