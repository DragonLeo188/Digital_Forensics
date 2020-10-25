import cv2 as cv
import sys
import imutils


def get_img(org_img):
    img = cv.imread(cv.samples.findFile(org_img))
    if img is None:
        print("Can't find the image.\n")
        sys.exit("Can't find the image.")
    img = imutils.resize(img, width=800)
    # cv.imshow(org_img, img)

    cv.waitKey(0)

    return img


def rsz_img(org_img, scale_percent):
    img = get_img(org_img)
    width = int(img.shape[1] * int(scale_percent) / 100)
    height = int(img.shape[0] * int(scale_percent) / 100)

    dsize = (width, height)

    resize_img = cv.resize(img, dsize)
    cv.imshow("Resize image: {}%".format(scale_percent), resize_img)
    cv.imwrite("char_test{}.png".format(scale_percent), resize_img)

    cv.waitKey(0)


def rslt(org_img, width, height):
    img = get_img(org_img)

    cv.imshow("Resolution of image: {0}x{1}".format(img.shape[0], img.shape[1]), img)
    cv.waitKey(0)


def dpi_modify(org_img, dpi):
    img = get_img(org_img)

    # Set width and height of images in inches
    width_inch = 4
    height_inch = 6

    # Set width and height of images in pixels
    width_pixels = int(width_inch * dpi)
    height_pixels = int(height_inch * dpi)

    dsize = (width_pixels, height_pixels)

    dpi_mod_img = cv.resize(img, dsize)

    cv.imshow("DPI: {}".format(dpi), dpi_mod_img)

    cv.waitKey(0)


# # Downsample by a factor of 2
rsz_img("chart_test.png", 50)
#
# # Downsample by a factor of 4
rsz_img("chart_test.png", 25)

# Resolution of image
rslt("LaRochelle.jpg", 300, 25)

# Modify DPI
dpi_modify("LaRochelle.jpg", 300)
dpi_modify("LaRochelle.jpg", 25)

# Effect of downsmapling image:
# - Images will lose details and not clear