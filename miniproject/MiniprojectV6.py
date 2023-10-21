import numpy as np
import cv2

def get_cell(x, y, res):
    cell_width = 500 // res
    cell_height = 500 // res
    cell_x = x // cell_width
    cell_y = y // cell_height
    return cell_x, cell_y

def print_coordinates_in_cells(contours, res):
    cell_centers = []

    for i, contour in enumerate(contours):
        # Find the center of mass of the object
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cell_x, cell_y = get_cell(cX, cY, res)

            if 0 <= cell_x < res and 0 <= cell_y < res:  # Ensure the contour is within the grid
                print(f"Object {i + 1} - Center Coordinates (x, y): ({cX}, {cY}), Cell: ({cell_x}, {cell_y})")
                cell_centers.append((cell_x, cell_y))

    return cell_centers

def categorize_hue(hue):
    if 20 <= hue < 30:
        return "Yellow"
    else:
        return "Other"

def compute_average_hsb(img, res, exclude_region):
    cell_hsbs = {}

    for x in range(res):
        for y in range(res):
            if exclude_region and (x >= 4 and y >= 4):
                continue

            cell_region = img[y * 500 // res: (y + 1) * 500 // res, x * 500 // res: (x + 1) * 500 // res]
            avg_color_hsv = cv2.cvtColor(np.uint8([[np.average(cell_region, axis=(0, 1))]]), cv2.COLOR_BGR2HSV)[0][0]
            cell_hsbs[(x, y)] = avg_color_hsv

    return cell_hsbs

# Load the image
img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res = 500

# Threshold the HSV image to isolate the yellow color
lower_yellow = np.array([20, 100, 175])  # Lower bound for yellow color in HSV
upper_yellow = np.array([30, 255, 255])  # Upper bound for yellow color in HSV
yellow_mask = cv2.inRange(img2, lower_yellow, upper_yellow)

# Find contours in the yellow mask
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print the number of yellow objects found
print(f"Number of yellow objects: {len(contours)}")

# Get cell positions for contours
cell_centers = print_coordinates_in_cells(contours, res)

# Draw rectangles around detected yellow objects and display the result
result_image = img.copy()
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    cell_x, cell_y = get_cell(x + w // 2, y + h // 2, res)
    if 0 <= cell_x < res and 0 <= cell_y < res:
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangles

# Create an array to mark cells containing objects
cells_with_objects = np.zeros((res, res), dtype=bool)

# Mark the cells containing objects
for cell_x, cell_y in cell_centers:
    cells_with_objects[cell_y, cell_x] = True

# Draw rectangles around cells containing objects
cell_size = 500 // res
for cell_x in range(res):
    for cell_y in range(res):
        if cells_with_objects[cell_y, cell_x]:
            x = cell_x * cell_size
            y = cell_y * cell_size
            cv2.rectangle(result_image, (x, y), (x + cell_size, y + cell_size), (0, 0, 255), 2)  # Draw red rectangles

# Calculate average HSB values for each cell (excluding the specified region)
exclude_region = False  # Set to True to exclude the region (x=400:500, y=400:500)
avg_hsbs = compute_average_hsb(img, res, exclude_region)

# Display HSB values for each cell
for cell_x in range(res):
    for cell_y in range(res):
        cell_hsb = avg_hsbs[(cell_x, cell_y)]
        cell_hue = cell_hsb[0]
        cell_color = categorize_hue(cell_hue)
        print(f"Cell ({cell_x}, {cell_y}) - Hue: {cell_hue}, Color: {cell_color}")

# Display the result image with rectangles
cv2.imshow("Result Image", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
