import cv2
import random
key = 0
a = [8,9,12,13,16,17,27]
random = random.randint(0,7)
print(a)
while(key != a[random]):
    
    img = cv2.imread("lion.jpg")
    cv2.imshow("???",img)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("????",img1)
    
    key = cv2.waitKey(1)
cv2.destroyAllWindows()
