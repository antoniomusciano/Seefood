import tkinter as tk
import random
from PIL import Image, ImageTk

# Show food on screen
# Ask user to

foods = ["apple", "orange", "banana"]


def food_selection():
    return random.choice(foods)


def picture_get():
    yee = food_selection()
    img_path = yee + ".png"
    img = ImageTk.PhotoImage(file=img_path)
    label.img = img  # Keep a reference to the image
    label.config(image=img)  # Set the image in the label


def on_button_click():
    label.config(text="Button Clicked!")


# Create the main window
window = tk.Tk()
window.title("SeeFood")
window.geometry('300x250')
window.resizable(False, False)

# Create a label to display the image and result
label = tk.Label(window, text="Click this button!")
label.pack()

# Call picture_get to initially display an image
picture_get()

# Create a button
button = tk.Button(window, text="Click Me!")  # Call picture_get when the button is clicked
button.place(x=125, y=20)



# Start the main loop
window.mainloop()
