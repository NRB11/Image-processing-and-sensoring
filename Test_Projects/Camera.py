import cv2
from pyzbar.pyzbar import decode
import time as t
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

height = 640
width = 480

cx = int(height / 2)
cy = int(width / 2)

hypo = 80

start_point = cx - hypo, cy - hypo
end_point = cx + hypo, cy + hypo

    
key = None

while (key != 27):
    _, frame = cap.read()
    
    #r = cv2.selectROI("select the area", frame)
    pixel_center_bgr = frame[cx, cy]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    #cv2.circle(frame, (cx,cy), 10, (255, 0, 0), 3)
    cv2.rectangle(frame, start_point, end_point, (0, 0, 255), 3)
    for code in decode(frame):
        QRCode = code.data.decode('utf-8')  
        match QRCode:
            case "4":
                print("Stoped") 
   
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1)
         
cap.release()
cv2.destroyAllWindows()