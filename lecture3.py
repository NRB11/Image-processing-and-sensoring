import cv2

key = 0

while(key != 27):
    
    img = cv2.imread("lion.png")
    cv2.show("???",img)
    key = cv2.waitKey(1)
cv2.destroyAllWindows()
