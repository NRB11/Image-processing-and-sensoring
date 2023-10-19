import struct
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def print_coordinates(contours):
    for i, contour in enumerate(contours):
        # Get the coordinates of the object
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        print(f"Object {i + 1} - Center Coordinates (x, y): ({cX}, {cY})")

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res = 500

coloraverages_red = np.zeros((res, res))
coloraverages_green = np.zeros((res, res))
coloraverages_blue = np.zeros((res, res))
for x in range(res):
    for y in range(res):
        avg_color_per_row = np.average(img[0 + x * int(500/res):int(500/res) + x * int(500/res), 0 + y * int(500/res):int(500/res) + y * int(500/res)], axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        coloraverages_red[x, y] = avg_color[2]
        coloraverages_green[x, y] = avg_color[1]
        coloraverages_blue[x, y] = avg_color[0]

average_color_image = np.dstack((coloraverages_red, coloraverages_green, coloraverages_blue))
normalized_color_averages = np.stack((coloraverages_red, coloraverages_green, coloraverages_blue), axis=-1) / 255.0

# Threshold the HSV image to isolate the yellow color
lower_yellow = np.array([20, 100, 180])  # Lower bound for yellow color in HSV
upper_yellow = np.array([30, 255, 255])  # Upper bound for yellow color in HSV
yellow_mask = cv2.inRange(img2, lower_yellow, upper_yellow)

# Find contours in the yellow mask
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print the number of yellow objects found
print(f"Number of yellow objects: {len(contours)}")

# Define the region (x=400:500, y=400:500) to exclude yellow detection
x_start, x_end, y_start, y_end = 400, 500, 400, 500

# Iterate through contours and print coordinates while excluding the specified region
for i, contour in enumerate(contours):
    # Extract the centroid of the object
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if not (x_start <= cX < x_end and y_start <= cY < y_end):
            print(f"Object {i + 1} - Center Coordinates (x, y): ({cX}, {cY})")

# Draw rectangles around detected yellow objects and display the result
result_image = img.copy()
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    if x_start <= x < x_end and y_start <= y < y_end:
        continue
    cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangles

plt.imshow(normalized_color_averages, interpolation='nearest')
cv2.imshow("Yellow Objects", result_image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()