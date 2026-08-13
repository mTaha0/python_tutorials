import cv2 as cv
import numpy as np


img = cv.imread('opencv_fundamentals/photos/cat.jpg')
blank = np.zeros((img.shape[:2]), dtype="uint8")
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
merged = cv.merge([b,g,r])


cv.imshow("b",b) # b değişkeni blue rengin değerine sahiptir, ekrana yazdırınca tek kanallı mavi değeri yazdırılır
cv.imshow("g",g)
cv.imshow("r",r)
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
cv.imshow("merged", merged)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)