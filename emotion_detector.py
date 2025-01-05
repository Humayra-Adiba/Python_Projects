import cv2


capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True:
    boolValue, frame = capture.read()
    gray_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_Frame = cv2.cvtColor(gray_Frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Emotion detector", rgb_Frame)
    faces = face_cascade.detectMultiScale(rgb_Frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 0, 225))


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()