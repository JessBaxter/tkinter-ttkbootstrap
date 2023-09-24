from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")


# Create button click function
def clicker():
    # ORIGINAL (Click button to select dropdown option)
    # Changed to a reset button, because we added click_bind for option selection
    # my_label.config(text=f"You clicked on {my_combo.get()}!")
    my_combo.current(0)  # Reset dropdown to Monday
    my_label.config(text="Hello world!")  # Reset my_label to "Hello world!"


# Create Binding function
# * (no need for extra 'select button',
# * because clicking item in dropdown auto-triggers)
# ? Need to pass in the e(vent) because clicking is an event
def click_bind(e):
    my_label.config(text=f"You clicked on {my_combo.get()}!")


# Create a label
my_label = tb.Label(root, text="Hello world!", font=("Helvetica", 18))
my_label.pack(pady=30)

# Create Dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create Combobox
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)

# Set Combo Default selection
my_combo.current(0)  # Monday


# Create a Button
# ORIGINAL
# my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="warning")
my_button = tb.Button(root, text="Reset", command=clicker, bootstyle="secondary")
my_button.pack(pady=20)

# Bind the combobox (no need for the Button)
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
