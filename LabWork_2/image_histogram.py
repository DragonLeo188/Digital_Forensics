import cv2 as cv
import sys
import imutils
import matplotlib.pyplot as plt
import numpy as np


def plotHistogram(img, histSize):
    channels = 0
    mask = None
    ranges = (0, 256)

    histogram = cv.calcHist([img], [channels], mask, [histSize], [0, 256])

    plt.plot(histogram)
    plt.show()


img = cv.imread("lena.png", cv.IMREAD_GRAYSCALE)
if img is None:
    print("Can't find the image.\n")
    sys.exit("Can't find the image.")
img = imutils.resize(img, width=800)

plotHistogram(img, 256)  # view the historgram on 256 levels
plotHistogram(img, 16)  # view the historgram on 16 levels
