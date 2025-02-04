#!/usr/bin/env python2

import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px from top-left to bottom-right corners
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. 
# This time we will draw a green rectangle at the top-right corner of image.
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# To draw a circle, you need its center coordinates and radius. 
# We will draw a circle inside the rectangle drawn above.
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# To draw the ellipse, we need to pass the major axis length and minor axis length.
# angle is the angle of rotation of ellipse in anti-clockwise direction. startAngle and
# endAngle denotes the starting and ending of ellipse arc measured in clockwise direction 
# from major axis. i.e. giving values 0 and 360 gives the full ellipse
# img = cv.ellipse(	img, center, axes, angle, startAngle, endAngle, color[,thickness[,lineType[,shift]]]	)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# To draw a polygon, first you need coordinates of vertices. Make those points into an array of shape ROWSx1x2 
# where ROWS are number of vertices and it should be of type int32. Here we draw a small polygon of with four 
# vertices in yellow color
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# print(pts)
pts = pts.reshape((-1,1,2))
print(pts)
img = cv2.polylines(img,[pts],True,(0,255,255)) # If third argument is False, you will get a polylines joining all the points, not a closed shape.


# To put texts in images, you need specify following things.

#         Text data that you want to write
#         Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
#         Font type (Check cv2.putText() docs for supported fonts)
#         Font Scale (specifies the size of font)
#         regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.

font = cv2.FONT_HERSHEY_SIMPLEX # write OpenCV on our image in white color.
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

print("done")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()