import cv2 as cv

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY )

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("thresholded_image", thresh)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("ınv_thresholded_image", thresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresholding", adaptive_thresh)

cv.waitKey(0)