import cv2 as cv
import numpy as np

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat", img)
blank = np.zeros((img.shape[0], img.shape[1], 3), dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#contours (Kontürler): Bu, resimde bulunan tüm kapalı şekillerin 
#koordinatlarını tutan devasa bir Python listesidir.
#(Hiyerarşi / Soyağacı): Bazı şekiller başka şekillerin içinde olabilir (örneğin iç içe geçmiş kareler
cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Kontor", blank)


print(f"{len(contours)} contour(s) found")
print(hierarchies)
print("-"*40)
print(contours)
cv.waitKey(0)
