import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

scale = 1
delta = 0
ddepth = cv.CV_16S

image = cv.imread("house8.png")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

image_blur = cv.blur(image_gray, (3, 3))

# Sobel operator
# Grandient X
grad_x = cv.Sobel(image, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
abs_grad_x = cv.convertScaleAbs(grad_x)

# Gradient Y
grad_y = cv.Sobel(image, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
abs_grad_y = cv.convertScaleAbs(grad_y)

sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

# Laplacian of Gaussian
laplacian = cv.Laplacian(image, ddepth, ksize=3)
laplacian = cv.convertScaleAbs(laplacian)

# Canny Edge detector
low_threshold = 25
ratio = 3
kernel_size = 3

detected_edges = cv.Canny(image_blur, low_threshold, low_threshold * ratio, kernel_size)
mask = detected_edges != 0
canny = image * (mask[:, :, None].astype(image.dtype))

plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobel, cmap='gray')
plt.title('Sobel'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(canny, cmap='gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()


