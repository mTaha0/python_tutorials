import cv2 as cv


img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat",img)

average = cv.blur(img, (8,8))
cv.imshow("averaged",average)

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("gauss", gauss)

median = cv.medianBlur(img, 7)
cv.imshow("median", median)

bilateral = cv.bilateralFilter(img, 5, 20, 50)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)