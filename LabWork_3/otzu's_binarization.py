import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

forme1 = cv.imread("forme1.png", cv.IMREAD_GRAYSCALE)
forme3 = cv.imread("forme3.png", cv.IMREAD_GRAYSCALE)
lena = cv.imread("lena.png", cv.IMREAD_GRAYSCALE)

cv.imshow("forme1", forme1)
cv.imshow("forme3", forme3)
cv.imshow("lena", lena)

cv.waitKey(0)

# Otsu's thresholding
ret, otzu_forme1 = cv.threshold(forme1, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
ret, otzu_forme3 = cv.threshold(forme3, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
ret, otzu_lena = cv.threshold(lena, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

cv.imshow("otzu_forme1", otzu_forme1)
cv.imshow("otzu_forme3", otzu_forme3)
cv.imshow("otzu_lena", otzu_lena)

cv.waitKey(0)

# Otsu's thresholding after Gaussian filtering
blur_forme1 = cv.GaussianBlur(forme1, (5, 5), 0)
ret,gaussian_otzu_forme1 = cv.threshold(blur_forme1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur_forme3 = cv.GaussianBlur(forme3, (5, 5), 0)
ret,gaussian_otzu_forme3 = cv.threshold(blur_forme3,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

blur_lena = cv.GaussianBlur(lena, (5, 5), 0)
ret,gaussian_otzu_lena = cv.threshold(blur_lena,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("gaussian_otzu_forme1", gaussian_otzu_forme1)
cv.imshow("gaussian_otzu_forme3", gaussian_otzu_forme3)
cv.imshow("gaussian_otzu_lena", gaussian_otzu_lena)

cv.waitKey(0)
