"""
Gerçek Zamanlı Nesne Tespiti ve Merkez İzleme (Real-time Object Detection and Centroid Tracking)

Bu program, bilgisayar kamerasından alınan video akışı üzerinde HSV renk uzayını kullanarak 
dinamik renk/nesne tespiti yapar. Tespit edilen nesnelerin sınırlarını (konturlarını) belirler 
ve matematiksel kütle merkezlerini (centroid) hesaplayarak ekranda işaretler.

Özellikler:
    - Dinamik Kalibrasyon: Dahili 'Ayarlar' penceresindeki Trackbar'lar sayesinde, 
      hedef nesnenin HSV renk sınırları (Hue, Saturation, Value) program çalışırken canlı olarak ayarlanabilir.
    - Arka Plan İzolasyonu: Maskeleme işlemi kullanılarak hedef nesne haricindeki 
      arka plan pikselleri izole edilir ve farklı bir renkle (kırmızı/pembe tonları) bastırılır.
    - Geometrik Analiz: cv.moments() fonksiyonu ile gürültüden arındırılmış (alanı 25 pikselden büyük) 
      şekillerin tam kütle merkezi hesaplanıp işaretlenir.
    - Birleşik Görselleştirme (Grid Display): İşlenmiş renkli sonuç görüntüsü ile 
      tespit edilen siyah-beyaz maske yan yana (np.hstack) tek bir pencerede birleştirilerek sunulur.

Kullanım:
    1. Programı çalıştırın.
    2. 'Ayarlar' penceresindeki çubukları kaydırarak yakalamak istediğiniz nesnenin rengine göre sınırları belirleyin.
    3. Çıkış yapmak için 'q' tuşuna basın.
"""

import cv2 as cv
import numpy as np

#trackbar'ın çalışması için boş fonksiyona ihtiyacımız var
def bos_fonksiyon(x):
    pass
cv.namedWindow('Ayarlar')
cv.resizeWindow('Ayarlar', 400, 250)
cv.createTrackbar('H_min', 'Ayarlar', 0, 179, bos_fonksiyon)
cv.createTrackbar('H_max', 'Ayarlar', 179, 179, bos_fonksiyon)
cv.createTrackbar('S_min', 'Ayarlar', 0, 255, bos_fonksiyon)
cv.createTrackbar('S_max', 'Ayarlar', 255, 255, bos_fonksiyon)
cv.createTrackbar('V_min', 'Ayarlar', 0, 255, bos_fonksiyon)
cv.createTrackbar('V_max', 'Ayarlar', 255, 255, bos_fonksiyon)

#her bir framedeki kontürleri tespit edip merkezine circle çizme fonksiyonu
def contour_point(img):
    islenmis_img = img.copy()
    islenmis_img = cv.flip(frame, 1)
    hsv = cv.cvtColor(islenmis_img, cv.COLOR_BGR2HSV)
    #track bar pozisyonları almak için 
    h_min = cv.getTrackbarPos('H_min', 'Ayarlar')
    h_max = cv.getTrackbarPos('H_max', 'Ayarlar')
    s_min = cv.getTrackbarPos('S_min', 'Ayarlar')
    s_max = cv.getTrackbarPos('S_max', 'Ayarlar')
    v_min = cv.getTrackbarPos('V_min', 'Ayarlar')
    v_max = cv.getTrackbarPos('V_max', 'Ayarlar')

    alt_sinir = np.array([h_min, s_min, v_min])
    üst_sinir = np.array([h_max, s_max, v_max])
    #sınır içi değerleri beyaz, kalanı siyah yapmak için
    mask = cv.inRange(hsv, alt_sinir, üst_sinir)
    mask = cv.medianBlur(mask, 5)
    hsv[mask == 0] = [180, 255, 255]
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    #bitwise = cv.bitwise_or(islenmis_img, hsv)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv.contourArea(contour) > 25:
            M = cv.moments(contour)

            if M['m00'] != 0:
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                cv.circle(bgr, (cX, cY), 10, (255, 0, 255), -1)
                cv.drawContours(bgr, [contour], -1, (255, 255, 0), 2)

    return bgr, mask

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Can't opened camera ! Exiting...")
    exit()

#FourCC, video sıkıştırma formatını (codec) işletim sistemine tanıtan koddur
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 30.0, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("Cant receive frame ! Exiting...")
        break

    result, mask = contour_point(frame)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    merged_window = np.hstack((result, mask))
    cv.imshow('Merged Window', merged_window)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()