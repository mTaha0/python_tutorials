import os
import cv2 as cv
import numpy as np

# img = cv.imread("opencv_fundamentals/photos/")
# cv.imshow("phtos", img)
# people = ["Ben Afflek", "Elton John", "", "", ""]

DIR = r'C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\photos\train'

folder_names = os.listdir(DIR)
features = []
labels = []
haar_cascade = cv.CascadeClassifier("opencv_fundamentals/haar_face.xml")

def createTrain():
    for person in folder_names:
        path = os.path.join(DIR, person)
        label = folder_names.index(person)

        for img in os.listdir(path):
            if img is None:
                continue

            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in face_rect:
                image_coor = gray[y:y+h, x:x+w]
                features.append(image_coor)
                labels.append(label)

createTrain()
print("Training done....")

features = np.array(features,dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)
face_recognizer.save('opencv_fundamentals/trained/face_trained.yml')
np.save('opencv_fundamentals/trained/features.npy', features)
np.save('opencv_fundamentals/trained/labels.npy', labels)