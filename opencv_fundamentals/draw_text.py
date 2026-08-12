import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype="uint8") #500x500 boyutunda,3 renk kanalı, uint8= resim
cv.imshow("blank", blank)

# blank[:] = 0, 255, 0 #green
# cv.imshow("green", blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)
#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1 )
cv.imshow("Circle", blank)
#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 0), thickness=3)
cv.imshow("Line", blank)
#put a text
cv.putText(blank, "hello world", (blank.shape[1]//2, blank.shape[0]//2), 
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2 )
cv.imshow("Text", blank)

cv.waitKey(0)