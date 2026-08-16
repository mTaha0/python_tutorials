import cv2 as cv
import numpy as np

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat",img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
# cv.Laplacian(gri_resim, veri_tipi)
# Yönsüz kenar bulucu. Ani renk değişimlerini yakalar. 
# Negatif (beyazdan siyaha) geçişleri kaybetmemek için cv.CV_64F geniş veri tipiyle kullanılır.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel
# cv.Sobel(gri_resim, veri_tipi, x_yonu, y_yonu)
# Yönlü kenar bulucu. x_yonu=1, y_yonu=0 verilirse sadece dikey kenarları; 
# x=0, y=1 verilirse sadece yatay kenarları bulur.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel', combined_sobel)

# canny 
# cv.Canny(gri_resim, alt_esik, ust_esik) 
# En gelişmiş kenar bulucu. Alt eşik altındakileri siler, üst eşik üstündekileri kesin kenar kabul eder.
# Arafta kalan zayıf çizgileri ise güçlü çizgilere temas ediyorsa kurtarır.
canny = cv.Canny(img, 125, 175 )
cv.imshow("Canny", canny)

cv.waitKey(0)