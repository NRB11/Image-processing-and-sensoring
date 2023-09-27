import cv2
import numpy as np
import struct

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

images = {}

for x in range(5):
    for y in range(5):
        images[struct.pack('ii', x, y)] = img2[0+x*100:100 + x*100, 0+y*100:100+y*100]
        if struct.pack('ii', x, y) in images:
            print(x, y, np.average(images[struct.pack('ii', x, y)]))
            
