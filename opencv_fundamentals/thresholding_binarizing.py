import cv2 as cv

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY )

# simple thresholding
# cv.threshold(gri_resim, esik_degeri, max_deger, kural_bayragi)
# Klasik eşikleme. Resimdeki pikseller esik_degeri'ni geçiyorsa onları max_deger (255) yapar, 
# geçemiyorsa siyah (0) yapar.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("thresholded_image", thresh)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("ınv_thresholded_image", thresh_inv)

# adaptive thresholding
# cv.adaptiveThreshold(gri_resim, max_deger, hesaplama_yontemi, kural, mahalle_boyutu, C_degeri)
# Akıllı eşikleme. Her pikselin geçme notunu, 
# etrafındaki (örn: 11x11) komşularının ortalamasından 'C' değerini çıkararak bölgesel hesaplar.
# Işık dalgalanmalarına karşı dirençlidir.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresholding", adaptive_thresh)

cv.waitKey(0)