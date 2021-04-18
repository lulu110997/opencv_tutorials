#!/usr/bin/env python2

import cv2

print("hi")
img = cv2.imread('babyYoda.png',-0)
print(img.shape)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
# cv2.imshow('frame',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()