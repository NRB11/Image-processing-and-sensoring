#Ml test for image recognition:
import cv2
import numpy as np
import tkinter as tk
import os
import csv

from PIL import Image, ImageTk

print("Wassup bitches!")

csv_file_path = "data.csv"
if not os.path.isfile(csv_file_path):
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Color", "Name"])  # Add a header row
else:
    with open(csv_file_path, "r") as csv_file:
        first_line = csv_file.readline().strip()
        if first_line == "":
            # If the file is empty, add the header
            with open(csv_file_path, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Color", "Name"])


def split_image(image, square_size):
    height, width, _ = image.shape
    squares = []

    for i in range(0, height, square_size):
        for j in range(0, width, square_size):
            square = image[i:i + square_size, j:j + square_size]
            squares.append(square)

    return squares

def store_data(color, name):
    pair_exists = False

    # Check if the CSV file exists
    csv_file_path = "data.csv"

    if not os.path.isfile(csv_file_path):
        # If the file doesn't exist, create it and add a header
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Color", "Name"])  # Add a header row

    with open("data.csv", "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

    with open("data.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([str(color), name])
def searchforcolor(color):
    with open("data.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            stored_color = eval(row[0])
            if(str(color) == str(row[0])):
                #print(str(color), str(row[0]), str(row[1]), "Match")
                return True
            #else:
                #print(str(color), str(row[0]), str(row[1]))
    return False

def label_object(square, name):
    # Create a Toplevel window to label objects
    toplevel = tk.Toplevel()

    def assign_label(label):
        avg_color = np.mean(square, axis=(0, 1))
        avg_color = avg_color.astype(int)
        formatted_color = f"[{avg_color[0]:3d}, {avg_color[1]:3d}, {avg_color[2]:3d}]"

        #print(f"Average Color (RGB): {formatted_color}")
        print(f"Square {name} labeled as '{label}', with color {formatted_color}")
        store_data(formatted_color,label)
        toplevel.destroy()  # Close the Toplevel window

    def closewindow():
        toplevel.destroy()  # Close the Toplevel window


    label = tk.Label(toplevel, text=f"Label the object in Square {name}")
    label.pack()

    square_image = ImageTk.PhotoImage(Image.fromarray(square))
    image_label = tk.Label(toplevel, image=square_image)
    image_label.photo = square_image  # Store a reference to the PhotoImage object
    image_label.pack()

    avg_color = np.mean(square, axis=(0, 1))
    avg_color = avg_color.astype(int)
    formatted_color = f"[{avg_color[0]:3d}, {avg_color[1]:3d}, {avg_color[2]:3d}]"

    if (searchforcolor(formatted_color)):
        closewindow()
        print("already logged", formatted_color)
    else:
        object_labels = ["Forest", "House", "Mountain_House", "Plains", "Huge_Crown", "Sand", "Water"]  # Add your object labels
        for obj_label in object_labels:
            button = tk.Button(toplevel, text=obj_label, command=lambda obj=obj_label: assign_label(obj))
            button.pack()
        # Keep the main menu window on top
        toplevel.transient(root)
        toplevel.grab_set()
        toplevel.focus_set()

def open_labeling_loop():
    # Load the image
    img = cv2.imread("miniproject/pictures/1.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height, width, channels = img.shape
    squares = split_image(img, int(width / 5))

    for i, square in enumerate(squares):
        label_object(square, i)


# Create the main application window
root = tk.Tk()
root.title("PROVE YOU ARE HUMAN MORTAL!")

# Create a white canvas as the platform
canvas = tk.Canvas(root, bg="black", width=600, height=400)
canvas.pack()
# Create a button on the canvas to initiate the labeling loop
button = tk.Button(root, text="Start The Captcha", command=open_labeling_loop)
button_window = canvas.create_window(50, 50, anchor="nw", window=button)  # Adjust the coordinates as needed

root.mainloop()  # Start the main application event loop