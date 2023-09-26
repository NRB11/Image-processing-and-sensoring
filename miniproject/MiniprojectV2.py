import cv2
import numpy as np

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

images = { #declare dictionary with stuff (same as hashmap)
    struct.pack('ii', 0, 0): img2[0:100, 0:100],
    struct.pack('ii', 1, 0): img2[0:100, 100:200],
    struct.pack('ii', 2, 0): img2[0:100, 200:300]

}