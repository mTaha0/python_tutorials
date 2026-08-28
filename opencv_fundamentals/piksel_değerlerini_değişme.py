import cv2 as cv
import numpy as np

img = cv.imread("opencv_fundamentals/photos/cat.jpg")
cv.imshow("cat", img)

alt_sinir = np.array([125, 125, 125])
üst_sinir = np.array([255, 255, 255])

mask = cv.inRange(img, alt_sinir, üst_sinir)

img[mask == 0] = [0, 0, 255]

cv.imshow("mask", mask)
cv.imshow("img", img)
cv.waitKey(0)
