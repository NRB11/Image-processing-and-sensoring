import cv2
import numpy as np
import math
#,cv2.COLOR_BGR2HSV
LetterPic = cv2.imread("letter.png")

Higth = 250
Width = 150
R = LetterPic[Higth,Width][2]
G = LetterPic[Higth,Width][1]
B = LetterPic[Higth,Width][0]
print(LetterPic[Higth,Width])
print(B)
print(G)
print(R)

top = (((R-G)+(R-B))/2)
print(top)

power = math.pow((R-G), 2)
print(power)

numberX = (power)+(R-B)*(G-B)
print(numberX)

bottom = math.sqrt(numberX)
print(bottom)

CalEQ = top/bottom

print(CalEQ)

Acos = np.arccos(CalEQ)

print(Acos)


LetterPic[250 , 200] = (0, 0, 255)
print("after modifyig",LetterPic[250 , 200])



cv2.imshow("letter", LetterPic)
cv2.waitKey(0)