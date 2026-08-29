"""
Gerçek Zamanlı El Takibi (Real-Time Hand Tracking) Modülü

Bu betik, bilgisayar kamerasından alınan canlı görüntü akışı üzerinde 
OpenCV ve MediaPipe kütüphanelerini kullanarak gerçek zamanlı el tespiti 
ve 21 noktalı eklem (landmark) takibi yapar.

Özellikler:
    * Görüntü Ön İşleme: Kameradan okunan kareler ayna etkisini kaldırmak 
      için yatay eksende (1) tersine çevrilir ve MediaPipe'ın çalışabilmesi 
      için BGR renk uzayından RGB'ye dönüştürülür.
    * El Tespiti: `mp.solutions.hands` modülü ile görüntüdeki eller tespit edilir.
    * Koordinat Dönüşümü: MediaPipe'ın ürettiği oransal koordinatlar (0.0 - 1.0), 
      pencerenin yükseklik ve genişlik değerleriyle çarpılarak gerçek piksel 
      koordinatlarına (cx, cy) dönüştürülür.
    * Görselleştirme: Tespit edilen eklemlerin üzerine siyah daireler çizilir 
      ve eklemler arası bağlantılar (HAND_CONNECTIONS) ekranda gösterilir.
    * FPS Hesaplama: İki kare arasında geçen süre (cTime - pTime) baz alınarak 
      Saniyedeki Kare Sayısı (FPS) hesaplanır ve ekrana yazdırılır.
Kullanım:
    Modülü doğrudan çalıştırdığınızda varsayılan kamera (0) açılacaktır.
    Video penceresi aktifken klavyeden 'q' tuşuna basılarak program 
    güvenli bir şekilde kapatılabilir.
"""

import cv2 as cv
import mediapipe as mp
import time
import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

if not cap.isOpened():
    print("Camera is not open !")
    exit()

while cap.isOpened():
    succes, frame = cap.read()
    if not succes:
        print("Can't receive a frame ! ")
        break

    frame = cv.flip(frame, 1)
    #bgr2rgb çünkü bu metot rgb uzayı ile çalışıyor
    frame_RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    #tespit ettiğimiz elleri result'a atadık
    results = hands.process(frame_RGB)
    print(results.multi_hand_landmarks)

    #birden fazla el varsa 
    if results.multi_hand_landmarks:
        for handsLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handsLms, mpHands.HAND_CONNECTIONS)
            #handmark'ların konumlarını elde etmek için
            for id, lm in enumerate(handsLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                cv.circle(frame, (cx, cy), 15, (0, 0, 0), cv.FILLED)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), thickness=3)

    cv.imshow("video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

