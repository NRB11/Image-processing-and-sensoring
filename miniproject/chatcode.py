import struct
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_cell(x, y, res):
    cell_width = 500 // res
    cell_height = 500 // res
    cell_x = x // cell_width
    cell_y = y // cell_height
    return cell_x, cell_y

def print_cells_of_contours(contours, res, exclude_region):
    cell_numbers = []

    for i, contour in enumerate(contours):
        # Find the center of mass of the object
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cell_x, cell_y = get_cell(cX, cY, res)

            if 0 <= cell_x < res and 0 <= cell_y < res and not (exclude_region[0] <= cX < exclude_region[1] and exclude_region[2] <= cY < exclude_region[3]):
                cell_number = cell_x + cell_y * res
                cell_numbers.append(cell_number)

    return cell_numbers

def compute_average_colors_hsv(image, res):
    cell_size = 500 // res
    avg_colors_hsv = []

    for cell_x in range(res):
        for cell_y in range(res):
            x = cell_x * cell_size
            y = cell_y * cell_size
            cell = image[y:y + cell_size, x:x + cell_size]

            # Compute the average color in HSV
            avg_color_hsv = np.mean(cv2.cvtColor(cell, cv2.COLOR_BGR2HSV), axis=(0, 1))
            avg_colors_hsv.append(avg_color_hsv)

    return avg_colors_hsv

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res = 5  # 5x5 grid, 25 cells

# Threshold the HSV image to isolate the yellow color
lower_yellow = np.array([20, 100, 180])  # Lower bound for yellow color in HSV
upper_yellow = np.array([30, 255, 255])  # Upper bound for yellow color in HSV
yellow_mask = cv2.inRange(img2, lower_yellow, upper_yellow)

# Find contours in the yellow mask
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define the region (x=400:500, y=400:500) to exclude yellow detection
exclude_region = (400, 500, 400, 500)

# Get cell numbers for contours while excluding the specified region
cell_numbers = print_cells_of_contours(contours, res, exclude_region)

# Create an array to mark cells containing objects
cells_with_objects = np.zeros((res, res), dtype=bool)

# Mark the cells containing objects
for cell_number in cell_numbers:
    cell_x = cell_number % res
    cell_y = cell_number // res
    cells_with_objects[cell_y, cell_x] = True

# Draw rectangles around cells containing objects
cell_size = 500 // res
result_image = img.copy()
for cell_x in range(res):
    for cell_y in range(res):
        if cells_with_objects[cell_y, cell_x]:
            x = cell_x * cell_size
            y = cell_y * cell_size
            cv2.rectangle(result_image, (x, y), (x + cell_size, y + cell_size), (0, 0, 255), 2)  # Draw red rectangles

# Draw contours in green
cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)

# Print the cell numbers containing objects
for cell_number in cell_numbers:
    print(f"Cell {cell_number} contains an object")

# Compute and display the average color of each cell in HSV
avg_colors_hsv = compute_average_colors_hsv(result_image, res)
for cell_number, avg_color_hsv in enumerate(avg_colors_hsv):
    print(f"Cell {cell_number} - Average Color (HSV): {avg_color_hsv}")

# Create a separate window to display the image with contours
#cv2.namedWindow("Cells with Objects and Contours", cv2.WINDOW_NORMAL)
cv2.imshow("Cells with Objects and Contours", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(normalized_color_averages, interpolation='nearest')
# plt.show()
