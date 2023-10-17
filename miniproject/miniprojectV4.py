
#Ml test for image recognition:
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

print("Wassup bitches!")


def split_image(image, square_size):
    height, width, _ = image.shape
    squares = []

    for i in range(0, height, square_size):
        for j in range(0, width, square_size):
            square = image[i:i + square_size, j:j + square_size]
            squares.append(square)

    return squares


# Create a list to store image references
image_references = []

def label_object(square, name):
    # Create a Toplevel window to label objects
    toplevel = tk.Toplevel()

    def assign_label(label):
        # Save the label for the square
        print(f"Square {name} labeled as '{label}'")
        toplevel.destroy()  # Close the Toplevel window

    label = tk.Label(toplevel, text=f"Label the object in Square {name}")
    label.pack()

    # Convert the square image to a PhotoImage object
    square_image = ImageTk.PhotoImage(Image.fromarray(square))

    image_label = tk.Label(toplevel, image=square_image)
    image_label.photo = square_image  # Store a reference to the PhotoImage object
    image_label.pack()

    # Add buttons for object labels
    object_labels = ["Object 1", "Object 2", "Object 3"]  # Add your object labels
    for obj_label in object_labels:
        button = tk.Button(toplevel, text=obj_label, command=lambda obj=obj_label: assign_label(obj))
        button.pack()

    # Keep the main menu window on top
    toplevel.transient(root)
    toplevel.grab_set()
    toplevel.focus_set()



# Create the main application window
root = tk.Tk()
root.title("Labeling Application")

# Create a white canvas as the platform
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

# Example usage:
def open_labeling_loop():
    # Load the image
    img = cv2.imread("miniproject/pictures/1.jpg")
    height, width, channels = img.shape
    squares = split_image(img, int(width / 5))

    for i, square in enumerate(squares):
        label_object(square, i)


# Create a button on the canvas to initiate the labeling loop
button = tk.Button(root, text="Start Labeling", command=open_labeling_loop)
button_window = canvas.create_window(50, 50, anchor="nw", window=button)  # Adjust the coordinates as needed

root.mainloop()  # Start the main application event loop