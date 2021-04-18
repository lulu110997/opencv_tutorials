#!/usr/bin/env python3

import cv2
import numpy as np 
from matplotlib import pyplot as plt

def GettingStarted():
	# Contours can be explained simply as a curve joining 
	# all the continuous points (along the boundary), having 
	# same color or intensity. The contours are a useful tool 
	# for shape analysis and object detection and recognition

	img1 = cv2.imread('star.jpg',0)
	img = cv2.blur(img1, (1,2))
	ret,thresh = cv2.threshold(img,127,255,1)
	contours, hierarchy = cv2.findContours(thresh, 1, 2)
	cnt = contours[1]
	img2 = cv2.drawContours(img, contours, -1, (0,255,0), 3) # draws all the countours in the image

	# method 1 for drawing indvidual contours
	# img2 = cv2.drawContours(img, contours, 3, (0,255,0), 3)
	# method 2 for drawing indvidual contours. Preffered
	# cnt = contours[4]
	# img2 = cv2.drawContours(img, [cnt], 0, (0,255 ,0), 3)

	cv2.imshow('contour', img2)
	cv2.imshow('img', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def ContourFeatures():
	# Image moments help you to calculate some features like center of mass of the object, area of the object etc.
	img1 = cv2.imread('star.jpg')
	img = cv2.blur(img1, (1,2))
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(img_gray,127,255,1)
	contours, hierarchy = cv2.findContours(thresh, 2, 1)
	cnt = contours[2]

	M = cv2.moments(cnt) # gives a dictionary of all moment values calculated
	print(cnt)

	# To find the centroid, area, perimeter 
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	# print(cx,cy)
	area = cv2.contourArea(cnt)
	# print(area)
	perimeter = cv2.arcLength(cnt,True)
	# print(perimeter)

	# Contour approximation: It approximates a contour shape to another shape with less number of vertices depending upon the 
	#  precision we specify. It is an implementation of Douglas-Peucker algorithm.
	epsilon = 0.1*cv2.arcLength(cnt,True) # maximum distance from contour to approximated contour. It is an accuracy parameter. A wise selection of epsilon is needed to get the correct output
	approx = cv2.approxPolyDP(cnt,epsilon,True)
	# print(approx)

	# Convex hull
	# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
	# points are the contours we pass into.
	# hull is the output, normally we avoid it.
	# clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise.
	# returnPoints : By default, True. Then it returns the coordinates of the hull points. If False, it returns the indices of contour points corresponding to the hull points.
	hull = cv2.convexHull(cnt)
	# print(hull)

	# Checing convexity. Function below will check if the curve is a convex or not and it will return a T or F bool
	k = cv2.isContourConvex(cnt)
	# print(k)

	# Sraight Bounding Rectangle
	# Straight rectangle that does not consider object rotation
	# Area of the bounding rectangle won't be minimum 
	# It is found by the function cv2.boundingRect()
	# Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
	x,y,w,h = cv2.boundingRect(cnt)
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

	# Rotating rectangle: bounding rectangle is drawn with minimum area, so it considers the rotation also
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	img = cv2.drawContours(img,[box],0,(1,1,1),2)
	# cv2.imshow('img', img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# Minumum enclosing circle: It is a circle which completely covers the object with minimum area
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius = int(radius)
	img3 = cv2.circle(img,center,radius,(255,255,255),2)
	# cv2.imshow('img', img3)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# Fit an ellipse around an object: It returns the rotated rectangle in which the ellipse is inscribed
	# ellipse = cv2.fitEllipse(cnt)
	# im = cv2.ellipse(im,ellipse,(0,255,0),2)

	# Fitting a line
	rows,cols = img.shape[:2]
	[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
	lefty = int((-x*vy/vx) + y)
	righty = int(((cols-x)*vy/vx)+y)
	img = cv2.line(img,(cols-1,righty),(0,lefty),(255,255,255),2)
	cv2.imshow('img', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def ContourProperties():
	img1 = cv2.imread('star.jpg')
	img = cv2.blur(img1, (1,2))
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(img_gray,127,255,0)
	contours, hierarchy = cv2.findContours(thresh, 2, 1)
	cnt = contours[0]

	# Aspect ratio: It is the ratio of width to height of bounding rect of the object.
	x,y,w,h = cv2.boundingRect(cnt)
	aspect_ratio = float(w)/h

	# Extent: Extent is the ratio of contour area to bounding rectangle area.
	area = cv2.contourArea(cnt)
	x,y,w,h = cv2.boundingRect(cnt)
	rect_area = w*h
	extent = float(area)/rect_area

	# Solidity is the ratio of contour area to its convex hull area
	area = cv2.contourArea(cnt)
	hull = cv2.convexHull(cnt)
	hull_area = cv2.contourArea(hull)
	solidity = float(area)/hull_area

	# Equivalent Diameter is the diameter of the circle whose area is same as the contour area
	area = cv2.contourArea(cnt)
	equi_diameter = np.sqrt(4*area/np.pi)

	# Orientation is the angle at which object is directed. Following method also gives the Major Axis and Minor Axis lengths
	(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
	
	# Mask and pixel points
	mask = np.zeros(img.shape,np.uint8)
	cv2.drawContours(mask,[cnt],0,255,-1)
	pixelpoints = np.transpose(np.nonzero(mask)) # np method: gives coordinates in (row, column)
	#pixelpoints = cv2.findNonZero(mask) # opencv method, gives coordinates in (x,y)

	# Maximum Value, Minimum Value and their locations
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img,mask = mask)

	# Mean color or mean intensity
	mean_val = cv2.mean(img,mask = mask)

	# Extreme Points means topmost, bottommost, rightmost and leftmost points of the object
	leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
	rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
	topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
	bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

def MoreFunction():
	
	img1 = cv2.imread('star.jpg')
	img = cv2.blur(img1, (1,2))
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(img_gray,127,255,1)
	contours, hierarchy = cv2.findContours(thresh, 2, 1)
	cnt = contours[2]

	# # Convexity Defects: Any deviation of the object from the convex hull can be considered as convexity defect
	# # hull = cv2.convexHull(cnt,returnPoints = False)
	# # defects = cv2.convexityDefects(cnt,hull) # have to pass returnPoints = False while finding convex hull, in order to find convexity defects
	# 										 # It returns an array where each row contains these values - [ start point, end point, farthest point, approximate distance to farthest point ]

	# hull = cv2.convexHull(cnt,returnPoints = False)
	# defects = cv2.convexityDefects(cnt,hull)

	# for i in range(defects.shape[0]):
	# 	s,e,f,d = defects[i,0]
	# 	start = tuple(cnt[s][0])
	# 	end = tuple(cnt[e][0])
	# 	far = tuple(cnt[f][0])
	# 	cv2.line(img,start,end,[0,255,0],2)
	# 	cv2.circle(img,far,5,[0,0,255],-1)

	# cv2.imshow('img',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	# # Point polygon function finds the shortest distance between a point in the image and a contour. returns the distance which is negative when point is outside the contour, positive when point is inside and zero if point is on the contour
	# dist = cv2.pointPolygonTest(cnt,(50,50),True) # If you don’t want to find the distance, make sure third argument is FalseIf you don’t want to find the distance, make sure third argument is False
	# print(int(dist))	

	# Match shapes: enables us to compare two shapes, or two contours and returns a metric showing the similarity. The lower the result, the better match it is
	rows, cols = img.shape[:2]
	rotationMatrix = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
	img2 = cv2.warpAffine(img_gray,rotationMatrix,(cols,rows))
	cv2.imshow('img', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	ret, thresh = cv2.threshold(img_gray, 127, 255,1)
	ret, thresh2 = cv2.threshold(img2, 127, 255,1)
	contours,hierarchy = cv2.findContours(thresh,1,2)
	cnt1 = contours[0]
	contours,hierarchy = cv2.findContours(thresh2,1,2)
	cnt2 = contours[0]

	ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
	print(ret)

def ContoursHierarchy():
	print("To do")

# GettingStarted()
# ContourFeatures()
# ContourProperties()
# MoreFunction()
ContoursHierarchy()