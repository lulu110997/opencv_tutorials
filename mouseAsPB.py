#!/usr/bin/env python2

import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i] # All available events for the mouse
print events

# Just a test to show how the waitKey function works. It essentially looks for which key is being pressed within
# the given time. If no key is pressed -1 is returned, but if a key is pressed, the code of that key is returned.
# We use bit multiplication with 255 to mask extraneous bits out 
# while(1):
# 	img = cv2.imread('babyYoda.png',0)
# 	cv2.imshow('image',img)
# 	k = cv2.waitKey(1) 
# 	print(k)
# 	if k & 0xFF == 27:
# 		break

# ##### Simple example
# # First we create a mouse callback function which is executed when a mouse event take place. 
# # Mouse event can be anything related to mouse like left-button down, left-button up, left-button 
# # double-click etc. It gives us the coordinates (x,y) for every mouse event. With this event and 
# # location, we can do whatever we like
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)

# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

##### Complex example
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) # bind this mouse callback function to OpenCV window

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()