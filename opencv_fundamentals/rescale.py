import cv2 as cv

img = cv.imread(r"C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\photos\cat.jpg")

def rescaleFrame(frame, scale=0.75):
    #images,videos and live videos
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #live videos only
    capture.set(3, width)
    capture.set(4,height)

new_frame = rescaleFrame(img)

cv.imshow("cat1", new_frame)
cv.imshow("cat2", img)

cv.waitKey(0)

#video rescaling
capture = cv.VideoCapture(r"C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\videos\dog.mp4")

while True:
    isTrue, frame = capture.read()

    if isTrue == False:
        break

    rescaled_frame = rescaleFrame(frame)
    cv.imshow("Dog1", frame)
    cv.imshow("Dog2", rescaled_frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
            break
    
capture.release()
cv.destroyAllWindows()