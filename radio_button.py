from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Radio Buttons")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x550")


# Create clicker function
def clicker():
    my_label.config(text=f"You selected: {my_topping.get()}")


# Create Radiobutton list
toppings = ["Pepperoni", "Cheese", "Veggie"]

# Create a Tkinter Variable to keep track of everything
my_topping = StringVar()

# Loop through the list and create radio buttons
# ? Can also do as a list of tuples: pepperoni and 1, cheese and 2 ...
for topping in toppings:
    tb.Radiobutton(  # not named as my_button because we're looping + using variables
        root,
        bootstyle="danger",
        variable=my_topping,  # Set the variable
        text=topping,  # The radio button text
        value=topping,  # my_topping variable will become Pepperoni
        command=clicker,  # OPTIONAL: negates having the "click me" button
    ).pack(pady=20)

# Create Button
my_button = tb.Button(root, text="Click me", command=clicker)
my_button.pack(pady=20)

# Create a Label
my_label = tb.Label(root, text="You selected: ")
my_label.pack(pady=20)

# =============================

# Create buttons that behave as radio buttons
# * These are still part of the other radio button list
# * Because we're using the my_topping variable
rb1 = tb.Radiobutton(
    root,
    bootstyle="info toolbutton",
    variable=my_topping,  # ! MAKE SURE THIS IS NOT IN "..."
    text="Radio Button 1",
    value="Radio Button 1",
    command=clicker,
)
rb1.pack(pady=20)
rb2 = tb.Radiobutton(
    root,
    bootstyle="info toolbutton",
    variable=my_topping,  # ! MAKE SURE THIS IS NOT IN "..."
    text="Radio Button 2",
    value="Radio Button 2",
    command=clicker,
)
rb2.pack(pady=20)
rb3 = tb.Radiobutton(
    root,
    bootstyle="info toolbutton outline",
    variable=my_topping,  # ! MAKE SURE THIS IS NOT IN "..."
    text="Radio Button 3",
    value="Radio Button 3",
    command=clicker,
)
rb3.pack(pady=20)

root.mainloop()
