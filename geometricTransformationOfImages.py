#!/usr/bin/env python2
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Preferable interpolation methods are 
# cv2.INTER_AREA for shrinking and 
# cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming
# cv2.INTER_LINEAR is the default

img = cv2.imread('babyYoda.png')
# res = cv2.resize(img,None,fx=int(1.2), fy=(1.2), interpolation = cv2.INTER_AREA)
# cv2.imshow('res',res )

#OR THE 'BETTER' METHOD CAUSE SHRINKING THE IMAGE USING THE METHOD ABOVE WILL GIVE AN ERROR

height, width = img.shape[:2]
res2 = cv2.resize(img,(int(0.5*width), int(0.5*height)), interpolation = cv2.INTER_AREA)
cv2.imshow('res2',res2 )
cv2.waitKey(0)
cv2.destroyAllWindows()

# Translation. You can take make it into a Numpy 
# array of type np.float32 and pass it into 
# cv2.warpAffine() function. See below example 
# for a shift of (100,50)

rows, cols = res2.shape[:2]
tranlationMatrix = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(res2,tranlationMatrix,(cols,rows))
cv2.imshow('translated image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotate the image by 90 degree with respect to center without any scaling.
scale = 1 # Rotation function gives the option to scale the image during rotation
rotationMatrix = cv2.getRotationMatrix2D((cols/2,rows/2),90,scale)
dst = cv2.warpAffine(res2,rotationMatrix,(cols,rows))
cv2.imshow('rotated image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Affine Transformation: all parallel lines in the original image will still be parallel in the output image
img = cv2.imread('sudoku.jpeg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# Perspective Transformation: Straight lines will remain straight even after the transformation
# 3x3 matrix is required
img = cv2.imread('sudoku.jpeg')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()