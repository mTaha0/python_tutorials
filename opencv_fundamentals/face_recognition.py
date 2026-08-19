import os 
import cv2 as cv
import numpy as np

DIR = r'C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\photos\train'
folder_names = os.listdir(DIR)

haar_cascade = cv.CascadeClassifier("opencv_fundamentals/haar_face.xml")
features = np.load("opencv_fundamentals/trained/features.npy", allow_pickle=True)
labels = np.load("opencv_fundamentals/trained/labels.npy", allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("opencv_fundamentals/trained/face_trained.yml")

img = cv.imread(r"C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\photos\val\ben_afflek\1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label is {folder_names[label]} with a confidence {confidence}")
    cv.putText(img, str(folder_names[label]), (50,50), cv.FONT_HERSHEY_COMPLEX, 3, (0,0,255), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected Face", img)
cv.waitKey(0)