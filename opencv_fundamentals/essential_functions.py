import cv2 as cv

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

#çizgileri belirginleştirmek için
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

#çizgileri incelttirmek için
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

cropped = img[50:250, 75:250]
cv.imshow("Cropped", cropped)

cv.waitKey(0)