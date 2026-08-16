import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#enumerate(), bir döngüde o anki elemanın hem indeks hem de listedeki değerini aynı anda almamızı sağlar

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)
bitwise_and = cv.bitwise_and(gray, gray, mask=mask)
gray_hist = cv.calcHist([gray], [0], bitwise_and, [256], [0,256])

colors = ("b", "g", "r")
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.imshow("mask", mask)
plt.figure()
plt.title("gray scale histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.show()



cv.imshow("Cat",img)
cv.waitKey(0)