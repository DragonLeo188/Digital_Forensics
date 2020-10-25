import cv2 as cv

forme1 = cv.imread("forme1.png", cv.IMREAD_GRAYSCALE)
house8 = cv.imread("house8.png", cv.IMREAD_GRAYSCALE)
woman = cv.imread("femme.png", cv.IMREAD_GRAYSCALE)

ret, forme1_thresh_bin = cv.threshold(forme1, 128, 255, cv.THRESH_BINARY)
ret, forme1_thresh_bin_inv = cv.threshold(forme1, 128, 255, cv.THRESH_BINARY_INV)

cv.imshow("forme1", forme1)
cv.imshow("forme1 threshold binary", forme1_thresh_bin)
cv.imshow("forme1 threshold binary inverse", forme1_thresh_bin_inv)

cv.waitKey(0)

ret, house8_thresh_bin = cv.threshold(house8, 96, 255, cv.THRESH_BINARY)
ret, house8_thresh_bin_inv = cv.threshold(house8, 96, 255, cv.THRESH_BINARY_INV)

cv.imshow("house8", house8)
cv.imshow("house8 threshold binary", house8_thresh_bin)
cv.imshow("house8 threshold binary inverse", house8_thresh_bin_inv)

cv.waitKey(0)

ret, woman_thresh_bin = cv.threshold(woman, 95, 255, cv.THRESH_BINARY)
ret, woman_thresh_bin_inv = cv.threshold(woman, 95, 255, cv.THRESH_BINARY_INV)

cv.imshow("woman", woman)
cv.imshow("woman threshold binary", woman_thresh_bin)
cv.imshow("woman threshold binary inverse", woman_thresh_bin_inv)

cv.waitKey(0)