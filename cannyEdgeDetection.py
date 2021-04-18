#!/usr/bin/env python3

import cv2
import numpy as np 
from matplotlib import pyplot as plt

# edge detection algo with the following steps
# 1 Noise reduction -> 2 finding intensity gradient of the image
# 3 non maximum suppresion -> 4 hysteresis thresholding
# cv2.Canny(). First argument is our input image. Second and 
# third arguments are our minVal and maxVal respectively. Third 
# argument is aperture_size. It is the size of Sobel kernel used 
# for find image gradients. By default it is 3. Last argument is 
# L2gradient which specifies the equation for finding gradient magnitude
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('babyYoda.png',0)
edges = cv2.Canny(img,0, 90, 7, L2gradient=True)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()