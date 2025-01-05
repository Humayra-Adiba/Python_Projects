import cv2
from pyzbar.pyzbar import decode
import time
# for default videocapture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
a = []
camera = True
while camera == True:
    sucess, frame = cap.read()
    for code in decode(frame):
        print(code.data.decode('utf-8'))
        a.append(code.data.decode('utf-8'))
        
        time.sleep(3)
    cv2.imshow('QR-code scan', frame)
    cv2.waitKey(4)
cap.release()
cv2.destroyAllWindows()