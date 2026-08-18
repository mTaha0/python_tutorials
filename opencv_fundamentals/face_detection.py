import cv2 as cv
import numpy as np

img = cv.imread("opencv_fundamentals/photos/human_faces_5.jpg")
cv.imshow("img", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("human face", gray)

# cv.CascadeClassifier(xml_dosya_yolu)
# Önceden eğitilmiş yüz tanıma modelini hafızaya yükler.
haar_cascade = cv.CascadeClassifier("opencv_fundamentals/haar_face.xml")

# model.detectMultiScale(gri_resim, kucultme_orani, min_onay_sayisi)
# Resimdeki yüzleri tarar ve bulduğu yüzlerin koordinatlarını (x, y, w, h) döndürür.
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
print(f"number of face in img : {len(face_rect)}")

# for (x,y,w,h) in liste:
# Bulunan her yüz koordinatı için döngüyle resmin üzerine çerçeve çizer.
for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected Faces", img)
cv.waitKey(0) 