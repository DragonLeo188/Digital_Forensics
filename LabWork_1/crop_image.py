import cv2 as cv
import sys


class crop_image:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def crop(self, title):
        crop_img = img[self.y1:self.y2, self.x1:self.x2]
        cv.imshow(title, crop_img)

        cv.waitKey(0)


img = cv.imread(cv.samples.findFile("football.jpeg"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

# purple_guy
x1_purple = 94
x2_purple = 184
y1_purple = 75
y2_purple = 240

purple_guy = crop_image(x1_purple, x2_purple, y1_purple, y2_purple)
purple_guy.crop("purple shirt guy")

# ball
x1_ball = 210
x2_ball = 235
y1_ball = 195
y2_ball = 224
ball = crop_image(x1_ball, x2_ball, y1_ball, y2_ball)
ball.crop("ball")

# red_guy
x1_red = 251
x2_red = 333
y1_red = 90
y2_red = 235

red = crop_image(x1_red, x2_red, y1_red, y2_red)
red.crop("red shirt guy")

cv.waitKey(0)
