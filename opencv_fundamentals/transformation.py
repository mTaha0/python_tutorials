import cv2 as cv
import numpy as np

img = cv.imread('opencv_fundamentals/photos/cat.jpg')
cv.imshow("Cat", img)

#Yeni X konumu = (1 * Eski X) + (0 * Eski Y) + Senin x değerin
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions) 
    #Afin dönüşüm (affine transformation), geometrik şekillerin veya uzaydaki 
    #noktaların doğrusal bir dönüşüm ile öteleme (kaydırma)

def rotation(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
     #verilen değerlere göre opencv fonksiyonu 
     #matris üretir
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

flip = cv.flip(img, -1)
cv.imshow("Flipped", flip)

translated = translate(img, 100,100)
cv.imshow("Translated Image", translated)

rotated = rotation(img, 90)
cv.imshow("Translated Image", rotated)


cv.waitKey(0)