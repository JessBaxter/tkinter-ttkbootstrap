from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")

# Create a Function for the Button
counter = 0


def changer():
    # ! FIX for "UnboundLocalError: cannot access local variable 'counter'
    # ! where it is not associated with a value"
    # * --> make variable global
    global counter
    counter += 1
    # if counter is an even number
    if counter % 2 == 0:
        my_label.config(text="Hello world!")
    # else, if odd
    else:
        my_label.config(text="Goodbye world!")


# Colours:
# Default, primary, secondary, success, info, warning, danger, light, dark

# Create a Label
# inverse --> adds background to text
my_label = tb.Label(
    text="Hello World!", font=("Helvetica", 28), bootstyle="default, inverse"
)
my_label.pack(pady=50)

# Create a Button
my_button = tb.Button(text="Click me", bootstyle="success, outline", command=changer)
my_button.pack(pady=20)

root.mainloop()
