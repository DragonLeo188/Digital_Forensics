import cv2 as cv
import sys
import numpy as np
import imutils

img = cv.imread(cv.samples.findFile("logo-usth.png"))
if img is None:
    print("Can't find the image.\n")
    sys.exit("Can't find the image.")
img = imutils.resize(img, width=800)
cv.imshow("USTH Logo", img)

b, g, r = cv.split(img)

# cv.imshow("Red channel", r)
# cv.imshow("Grey channel", g)
# cv.imshow("Blue channel", b)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# color range
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
# blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
# blue_mask = imutils.resize(blue_mask, width=800)
# cv.imshow("Blue mask", blue_mask)
lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])
blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
blue_mask = cv.bitwise_and(img, img, mask=blue_mask)
blue_mask = imutils.resize(blue_mask, width=800)

cv.imshow("Blue mask", blue_mask)

# lower_red = np.array([170,50,50])
# upper_red = np.array([180,255,255])
# red_mask = cv.inRange(hsv, lower_red, upper_red)
# red_mask = imutils.resize(red_mask, width=800)
# cv.imshow("Red mask", red_mask)

lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])
red_mask = cv.inRange(hsv, lower_red, upper_red)
red_mask = cv.bitwise_and(img, img, mask=red_mask)
red_mask = imutils.resize(red_mask, width=800)

cv.imshow("Red mask", red_mask)

k = cv.waitKey(0)
