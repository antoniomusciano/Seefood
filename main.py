import tkinter as tk
import random


def on_button_click():
    label.config(text="Button Clicked!")
    # print(food_selection())


# Create the main window
window = tk.Tk()
window.title("SeeFood")
window.geometry('300x250')
window.resizable(False, False)

# Create a button
button = tk.Button(window, text="Click Me!", command=on_button_click)
button.place(x=125, y=20)

# Create a label to display the result
label = tk.Label(window, text="Click this button!")
label.pack()

# Start the main loop
window.mainloop()
