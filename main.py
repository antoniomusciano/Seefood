import tkinter as tk
from tkinter import Label, Entry
import random
from PIL import Image, ImageTk

foods = ["apple", "orange", "banana"]
selected_food = ""  # Initialize the variable to store selected food globally

def food_selection():
    global selected_food
    selected_food = random.choice(foods)
    e.delete(0, tk.END)  # Clear the current entry content
    e.insert(0, "Enter the food shown below: ")  # Set the selected food in the entry
    picture_get(selected_food)

def picture_get(s_f):
    img_path = s_f + ".png"
    img = ImageTk.PhotoImage(file=img_path)
    label.img = img  # Keep a reference to the image
    label.config(image=img)  # Set the image in the label
    label.image = img  # Keep a reference to the image
    label.pack()  # Re-pack the label to ensure it's displayed in front

def on_button_click():
    user_input = e.get().lower()  # Convert user input to lowercase for case-insensitivity
    selected_food_lower = selected_food.lower()  # Convert selected food to lowercase for case-insensitivity
    print(user_input)

    if user_input == selected_food_lower:
        result_text = "Correct! You guessed it!"
        result_label = Label(window, text=result_text, font=("Courier 14 bold"), fg="green")
        print('yup')
    else:
        
        result_text = f"Wrong! The correct answer is {selected_food}."
        result_label = Label(window, text=result_text, font=("Courier 14 bold"), fg="red")
        
    result_label.pack()
    window.after(2000, lambda: result_label.pack_forget())  # Display the result for 2 seconds and then hide it
    food_selection()

def quit():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("SeeFood")
window.geometry('300x250')
window.resizable(True, True)
window.attributes('-fullscreen', True)

# Create an Entry widget to accept User Input
e = Entry(window, width=50)
e.pack()

# Initialize a Label to display the User Input
label = Label(window, text="", font=("Courier 22 bold"))
label.pack()

# Call picture_get to initially display an image
food_selection()

# Create a button
button = tk.Button(window, text="Final Answer?", command=on_button_click)
button.pack(pady=20)


button= tk.Button(window,text="Quit", font=('Comic Sans', 13, 'bold'), command= quit)
button.pack(pady=50)

# Start the main loop
window.mainloop()
