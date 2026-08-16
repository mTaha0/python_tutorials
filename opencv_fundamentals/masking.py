import cv2 as cv
import numpy as np

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
blank = np.zeros(img.shape[:2], dtype="uint8") 
mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 20, img.shape[0]//2 + 20),
                    100, 50, -1 )
# cv.bitwise_and(resim1, resim2, mask=maske_resmi)
# Maskeleme yapar. İki resmi piksel piksel karşılaştırır, sadece ikisinde de beyaz olan yerleri (kesişimi) renkli tutar.
bitwise_and = cv.bitwise_and(img, img, mask=mask)

cv.imshow("img", img)
cv.imshow("mask", mask)
cv.imshow("bitwise_and",bitwise_and)

cv.waitKey(0)