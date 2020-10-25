import cv2 as cv
import matplotlib.pyplot as plt


def plotHistogram(img, histSize):
    channels = 0
    mask = None
    ranges = (0, 256)

    histogram = cv.calcHist([img], [channels], mask, [histSize], [0, 256])

    plt.plot(histogram)
    plt.show()


forme3 = cv.imread("forme3.png", cv.IMREAD_GRAYSCALE)
plotHistogram(forme3, 256)
ret, forme3_thresh_bin = cv.threshold(forme3, 128, 255, cv.THRESH_BINARY)
cv.imshow("forme1 threshold binary", forme3_thresh_bin)

