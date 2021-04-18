#!/usr/bin/env python

import cv2

########################## video playback from camera ##############################

# Creates a video capture object that captures the video (ie camera object)
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    # ret returns a bool to see if frame is being correctly read
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Colour codes https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html
    code1 = cv2.cvtColor(frame, 1)

    # Display the resulting frame
    cv2.imshow('frame', code1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

########################## video playback from file ##############################

# cap = cv2.VideoCapture('testVideoBaby.webm')

# while(cap.isOpened()):
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(100) & 0xFF == ord('q'): # Wait key will dictate how long the video will play
#         break

# cap.release()
# cv2.destroyAllWindows()


########################## save recording from camera ##############################

# cap = cv2.VideoCapture(4)

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)

#         # write the flipped frame
#         out.write(frame)

#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
