import cv2 as cv

#reading an image
img = cv.imread(r"C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\photos\cat.jpg")
cv.imshow("Cat",img)
cv.waitKey(0)

capture = cv.VideoCapture(r"C:\Users\tahat\Desktop\python_tutorials\opencv_fundamentals\videos\dog.mp4")
# Capture, içinde renk, piksel veya NumPy matrisi barındırmaz. 
# #Sadece o dosyayı oynatmak, durdurmak veya özelliklerini 
# (videonun uzunluğu, FPS değeri vb.) okumak için kullandığın bir araçtır (objedir).

print(capture)
while True:
    isTrue, frame = capture.read()

    if isTrue == False:
        break
    
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()