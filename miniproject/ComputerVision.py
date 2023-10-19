import cv2
import numpy as np

# Load the image
image_path = 'miniproject/pictures/1.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Define the coordinates of the top-left and bottom-right corners of the 100x100 pixel square
top_left = (300, 100)  # Replace with the desired coordinates
bottom_right = (400, 200)  # Replace with the desired coordinates

# Crop the square from the original image
square = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

# Define the lower and upper bounds for the yellow color in BGR format
lower_yellow = np.array([0, 100, 100])
upper_yellow = np.array([40, 255, 255])

# Convert the square to the HSV color space
square_hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

# Create a mask to extract the yellow pixels
yellow_mask = cv2.inRange(square_hsv, lower_yellow, upper_yellow)

# Find the yellow color within the square
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
    print("Yellow color found in the 100x100 pixel square.")
else:
    print("No yellow color found in the 100x100 pixel square.")

# Display the square and the yellow mask (for visual confirmation)
cv2.imshow("Square", square)
cv2.imshow("Yellow Mask", yellow_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
