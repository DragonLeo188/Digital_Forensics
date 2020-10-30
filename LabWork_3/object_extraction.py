import cv2 as cv
import sys
import imutils
from matplotlib import pyplot as plt
import numpy as np


def show_img(org_img):
    img = cv.imread(cv.samples.findFile(org_img), cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Can't find the image.\n")
        sys.exit("Can't find the image.")
    img = imutils.resize(img, width=800)

    return img


def abitrary_binary(img):
    blur = cv.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv.threshold(img, 130, 255, cv.THRESH_BINARY_INV)

    return th3


def thick_wall():
    img = show_img("cadastre2.png")

    kernel = np.ones((5, 5), np.uint8)
    for i in range(5):
        thickWall = cv.morphologyEx(abitrary_binary(img), cv.MORPH_OPEN, kernel)

    return thickWall


def thin_wall():
    img = show_img("cadastre2.png")

    ret, wall = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    ret, thickWall = cv.threshold(wall, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    thickWall = cv.dilate(thickWall, kernel, iterations=1)

    thinWall = wall - thickWall
    ret, thinWall = cv.threshold(thinWall, 0, 255, cv.THRESH_BINARY_INV)

    return thinWall


img = show_img("cadastre2.png")

titles = ['Original Image', 'Thick Wall', 'Thin Wall']
images = [img, thick_wall(), thin_wall()]
for i in range(len(titles)):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

