import cv2
import numpy as np
import struct

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

"""dictionary
    
images = { #declare dictionary with stuff (same as hashmap)
    struct.pack('ii', 0, 0): img2[0:100,   0:100],
    struct.pack('ii', 1, 0): img2[0:100, 100:200],
    struct.pack('ii', 2, 0): img2[0:100, 200:300],
    struct.pack('ii', 3, 0): img2[0:100, 300:400],
    struct.pack('ii', 4, 0): img2[0:100, 400:500],
    
    struct.pack('ii', 0, 1): img2[100:200,   0:100],
    struct.pack('ii', 1, 1): img2[100:200, 100:200],
    struct.pack('ii', 2, 1): img2[100:200, 200:300],
    struct.pack('ii', 3, 1): img2[100:200, 300:400],
    struct.pack('ii', 4, 1): img2[100:200, 400:500],
    
    struct.pack('ii', 0, 2): img2[200:300,   0:100],
    struct.pack('ii', 1, 2): img2[200:300, 100:200],
    struct.pack('ii', 2, 1): img2[200:300, 200:300],
    struct.pack('ii', 3, 1): img2[200:300, 300:400],
    struct.pack('ii', 4, 1): img2[200:300, 400:500],
    
    struct.pack('ii', 0, 3): img2[300:400,   0:100],
    struct.pack('ii', 1, 3): img2[300:400, 100:200],
    struct.pack('ii', 2, 3): img2[300:400, 200:300],
    struct.pack('ii', 3, 3): img2[300:400, 300:400],
    struct.pack('ii', 4, 3): img2[300:400, 400:500],
    
    struct.pack('ii', 0, 4): img2[400:500,   0:100],
    struct.pack('ii', 1, 4): img2[400:500, 100:200],
    struct.pack('ii', 2, 4): img2[400:500, 200:300],
    struct.pack('ii', 3, 4): img2[400:500, 300:400],
    struct.pack('ii', 4, 4): img2[400:500, 400:500],
}

for x in range(5):
    for y in range(5):
        if struct.pack('ii', x, y) in images:
            print(x, y, np.average(images[struct.pack('ii', x, y)]))
"""
images = {}

for x in range(5):
    for y in range(5):
        images[struct.pack('ii', x, y)] = img2[0+x*100:100 + x*100, 0+y*100:100+y*100]
        if struct.pack('ii', x, y) in images:
            print(x, y, np.average(images[struct.pack('ii', x, y)]))