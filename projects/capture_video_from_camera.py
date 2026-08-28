import cv2 as cv
import numpy as np

alt_sinir = np.array([0, 0, 40])
üst_sinir = np.array([180, 255, 255])

def contour_point(img):
    islenmis_img = img.copy()
    islenmis_img = cv.flip(frame, 1)
    hsv = cv.cvtColor(islenmis_img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, alt_sinir, üst_sinir)
    mask = cv.medianBlur(mask, 5)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    copy = hsv.copy()

    for contour in contours:
        if cv.contourArea(contour) > 50:
            M = cv.moments(contour)

            if M['m00'] != 0:
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                cv.circle(copy, (cX, cY), 10, (0, 0, 255), -1)
                cv.drawContours(copy, [contour], -1, (0, 255, 0), 2)


    hsv[mask == 0] = [255, 0, 0]

    return islenmis_img, mask

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

    sonuc, maske = contour_point(frame)
    cv.imshow("sonuc", sonuc)
    cv.imshow('maske', maske)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


