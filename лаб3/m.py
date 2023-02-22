import cv2


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#включаем вебкамеру
video_capture = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('web_cams.avi',codec, 24.0, (640,480))

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    #рисование прямоугольника
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

    #вывод в окно
    cv2.imshow('Video', frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        #выход
        break
    elif k%256 == 32:
        #скриншот камеры
        cv2.imwrite("screenshot.jpg", frame)
    
    #запись видео    
    out.write(frame)    

#релиз 
out.release()
video_capture.release()
cv2.destroyAllWindows()