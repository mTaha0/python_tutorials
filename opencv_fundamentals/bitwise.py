import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8" )

# cv.rectangle(resim, sol_ust_kose, sag_alt_kose, renk, kalinlik) 
# Resme dikdörtgen çizer. Kalınlık parametresine -1 verilirse karenin içini tamamen doldurur.
rectangle = cv.rectangle(blank.copy(), (100, 100), (400, 400), 255, -1)
circle = cv.circle(blank.copy(), (250, 250), 175, 255, -1)

bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
bitwise_not = cv.bitwise_not(rectangle)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)
cv.imshow("bitwise", bitwise_and)
cv.imshow("bitwise_or", bitwise_or)
cv.imshow("bitwise_xor", bitwise_xor)
cv.imshow("bitwise_not", bitwise_not)


cv.waitKey(0)