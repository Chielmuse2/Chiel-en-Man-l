import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Set the window size (optional)
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Path to your background image
image_path = r"images/crowd.png"  # Replace with the actual path to your image

# Open the image using Pillow
bg_image = Image.open(image_path)

# Resize the image to fit the window size (optional)
bg_image = bg_image.resize((800, 600))  # Resize to fit the window size

# Convert the image to a format that Tkinter can use
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to act as the background
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window

# Now you can add other widgets on top of the background
label = tk.Label(root, text="This is a label over the background", fg="white", font=("Arial", 20))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", font=("Arial", 14))
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()