import cv2
import numpy

python_logo = cv2.imread("tinypic.png")
print(f"Type of variable: {type(python_logo)}")
print(f"Type of data in array: {python_logo.dtype}")
print(f"Shape of array: {python_logo.shape}")

pixel_value = python_logo[2, ] # B, G, R
print(pixel_value)

# Slicing
logo_cropped = python_logo.copy()
logo_cropped = logo_cropped[50:150, :]

logo_cropped[30, 30] = [0, 0, 255]

cv2.imshow("Original logo", python_logo)
cv2.imshow("Cropped logo", logo_cropped)
cv2.waitKey(0)