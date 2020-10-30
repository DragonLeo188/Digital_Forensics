from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
import sys
import imutils


def show_img(org_img):
    img = cv.imread(cv.samples.findFile(org_img), cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Can't find the image.\n")
        sys.exit("Can't find the image.")
    # img = imutils.resize(img, width=800)

    return img


img = cv.imread('cadastre1.png', cv.IMREAD_GRAYSCALE)

kernel = np.ones((1, 1), np.uint8)
text = cv.erode(img, kernel, iterations=100)

text = cv.morphologyEx(text, cv.MORPH_CROSS, kernel)

text = cv.GaussianBlur(text, (1, 1), 0)
ret, text = cv.threshold(text, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

text = cv.morphologyEx(text, cv.MORPH_OPEN, kernel)

titles = ['Original Image', 'Text']
images = [img, text]
for i in range(len(titles)):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
