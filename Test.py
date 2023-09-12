import cv2

GetColor = cv2.imread("tinypic.png")
print(GetColor[2,2,])

cv2.imshow("Original", GetColor)
cv2.waitKey(0)