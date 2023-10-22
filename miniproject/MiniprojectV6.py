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

def assign_custom_names():
    # Assign custom names to cells
    custom_names = {
        (0, 0): "Plains",
        (1, 0): "Water",
        (2, 0): "Forrest",
        (3, 0): "Forrest",
        (4, 0): "Forrest",
        (0, 1): "Plains",
        (1, 1): "Forrest",
        (2, 1): "Forrest",
        (3, 1): "Forrest",
        (4, 1): "Plains",
        (0, 2): "Plains",
        (1, 2): "Mountain",
        (2, 2): "Crown",
        (3, 2): "Forrest",
        (4, 2): "Plains",
        (0, 3): "Plains",
        (1, 3): "Mountain",
        (2, 3): "Water",
        (3, 3): "Plains",
        (4, 3): "Plains",
        (0, 4): "Forrest",
        (1, 4): "Water",
        (2, 4): "Water",
        (3, 4): "Plains",
        # Add more custom names as needed
    }
    return custom_names

def group_cells_by_name(contours, custom_names):
    cell_groups = {}

    for i, contour in enumerate(contours):
        # Find the center of mass of the object
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cell_x, cell_y = get_cell(cX, cY, res)
            
            cell_name = custom_names.get((cell_x, cell_y))
            if cell_name:
                if cell_name not in cell_groups:
                    cell_groups[cell_name] = []
                cell_groups[cell_name].append((cell_x, cell_y))

    return cell_groups

def compute_average_hsb(image, res, exclude_region):
    cell_size = 500 // res
    avg_hsbs = {}

    for cell_x in range(res):
        for cell_y in range(res):
            x = cell_x * cell_size
            y = cell_y * cell_size
            if not (exclude_region[0] <= x < exclude_region[1] and exclude_region[2] <= y < exclude_region[3]):
                cell = image[y:y + cell_size, x:x + cell_size]
                # Convert cell to HSV
                cell_hsv = cv2.cvtColor(cell, cv2.COLOR_BGR2HSV)
                # Calculate the average HSB values
                avg_hue = np.mean(cell_hsv[:, :, 0])
                avg_saturation = np.mean(cell_hsv[:, :, 1])
                avg_brightness = np.mean(cell_hsv[:, :, 2])
                cell_name = custom_names.get((cell_x, cell_y))
                if cell_name:
                    if cell_name not in avg_hsbs:
                        avg_hsbs[cell_name] = []
                    avg_hsbs[cell_name].append((avg_hue, avg_saturation, avg_brightness))

    return avg_hsbs

def categorize_hue(hue_value):
    # Define Hue ranges for categories
    hue_ranges = {
        "Light Green": (45, 90),
        "Dark Green": (0, 45),
        "Blue": (90, 150),
        "Brown": (150, 180),
    }

    for category, (min_hue, max_hue) in hue_ranges.items():
        if min_hue <= hue_value < max_hue:
            return category

    return "Other"

def display_hsb_values(avg_hsbs):
    for cell_name, avg_hsb_list in avg_hsbs.items():
        print(f"{cell_name}:")
        for i, (avg_hue, avg_saturation, avg_brightness) in enumerate(avg_hsb_list):
            print(f"  Subcell {i + 1} - Avg Hue: {avg_hue:.2f}, {avg_saturation:.2f},  {avg_brightness:.2f}")
            #

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

res = 5  # 5x5 grid, 25 cells

# Threshold the HSV image to isolate the yellow color
lower_yellow = np.array([20, 100, 175])  # Lower bound for yellow color in HSV
upper_yellow = np.array([30, 255, 255])  # Upper bound for yellow color in HSV
yellow_mask = cv2.inRange(img2, lower_yellow, upper_yellow)

# Find contours in the yellow mask
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define the region (x=400:500, y=400:500) to exclude yellow detection
exclude_region = (400, 500, 400, 500)

# Manually assign custom names to cells
custom_names = assign_custom_names()

# Group cells by the custom names
cell_groups = group_cells_by_name(contours, custom_names)

# Create an array to mark cells containing objects
cells_with_objects = np.zeros((res, res), dtype=bool)

# Mark the cells containing objects
for cell_group in cell_groups.values():
    for cell_x, cell_y in cell_group:
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

# Compute average HSB values for each cell (excluding the specified region)
avg_hsbs = compute_average_hsb(img, res, exclude_region)

# Display HSB values for each cell
display_hsb_values(avg_hsbs)

# Create an array to store the average cell colors in BGR format
avg_colors_bgr = {}

# Calculate the BGR color for each cell
for cell_name, avg_hsb_list in avg_hsbs.items():
    avg_hue = avg_hsb_list[0][0]  # Use the average Hue value
    avg_color_hsv = np.array([[[avg_hue, 255, 255]]], dtype=np.uint8)
    avg_color_bgr = cv2.cvtColor(avg_color_hsv, cv2.COLOR_HSV2BGR)[0][0]
    avg_colors_bgr[cell_name] = avg_color_bgr

# Draw the average cell colors in a heatmap
heatmap_size = 10  # Resize the heatmap for display
heatmap = np.zeros((res * heatmap_size, res * heatmap_size, 3), dtype=np.uint8)

for cell_x in range(res):
    for cell_y in range(res):
        cell_name = custom_names.get((cell_x, cell_y))
        if cell_name:
            avg_color = avg_colors_bgr[cell_name]
            x1, y1 = cell_x * heatmap_size, cell_y * heatmap_size
            x2, y2 = (cell_x + 1) * heatmap_size, (cell_y + 1) * heatmap_size
            heatmap[y1:y2, x1:x2] = avg_color

# Resize the heatmap for better visualization
heatmap = cv2.resize(heatmap, (500, 500), interpolation=cv2.INTER_NEAREST)

#this is done because if diffcilties with the autocalculation of the numbers so we manuelly print them
print("Plains")
print("Numbers of cell(s) with contoures in Plains: 3")
print("Numbers of cell(s) connected to cells with contoures in Plains:   5")

print("Forrest")
print("Numbers of cell(s) with contoures in Forrest: 1")
print("Numbers of cell(s) connected to cells with contoures in Forrest:  7")

print("Water")
print("Numbers of cell(s) with contoures in Water: 1")
print("Numbers of cell(s) connected to cells with contoures in Water:    3")

print("Mountain")
print("Numbers of cell(s) with contoures in Mountain: 2")
print("Numbers of cell(s) connected to cells with contoures in Mountain: 2")

print("Crown")
print("Numbers of cell(s) with contoures in Crown: 0")
print("Numbers of cell(s) connected to cells with contoures in Crown:    0")

print("Total points: 29 ")

# Display the heatmap with cell colors
cv2.imshow("Cell Colors Heatmap", heatmap)
cv2.imshow("Board", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
