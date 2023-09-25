# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/api/validation/
# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/cookbook/validate-user-input/
# API: https://ttkbootstrap.readthedocs.io/en/latest/api/

# [...] = A list - mutable
# (...) = A tuple - immutable

from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/
from ttkbootstrap.dialogs import Messagebox  # ! Required for Messagebox

# from datetime import date  # Allows you to set startdate in tb.DateEntry()
# from ttkbootstrap.dialogs import Querybox  # Allows Button to bring up calendar

root = tb.Window(themename="superhero")
# LIGHT: https://ttkbootstrap.readthedocs.io/en/latest/themes/light/
# DARK: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/

# root = Tk()
root.title("TTK Bootstrap: Message Box")
# Main app icon
# root.iconbitmap('images/codemy.ico')
# ! Messagebox Icon -> need BOTH this and Main app icon
# root.iconbitmap(default='images/codemy.ico')
root.geometry("700x350")


# Create yesno function
# * Shows YES and NO buttons
def yesno():
    # Create a dialog
    # yesno
    # ! NEED IMPORT: from ttkbootstrap.dialogs import Messagebox
    messagebox = Messagebox.yesno("Does pineapple belong on pizza?", "Voting time!")

    # Set Label to show which button was clicked
    if messagebox == "No":  # When using Messagebox.yesno
        my_label.config(text=f"You clicked: {messagebox} ❌")
    elif messagebox == "Yes":
        my_label.config(text=f"You clicked: {messagebox} ✔")
    else:
        my_label.config(text=f"You closed the window {messagebox}")


# Create ok function
# * Only shows OK button
def ok():
    # ok
    messagebox = Messagebox.ok("What do you think?", "Voting time!")

    # Set Label to show which button was clicked
    my_label.config(text=f"You clicked: {messagebox}")


# Create okcancel function
# * Shows OK and CANCEL buttons
def okcancel():
    # ok
    messagebox = Messagebox.okcancel("Proceed or gtfo?", "Voting time!")

    # Set Label to show which button was clicked
    if messagebox == "Cancel":  # When using Messagebox.okcancel
        my_label.config(text=f"You clicked CANCEL (value = {messagebox})")
    elif messagebox == "OK":
        my_label.config(text=f"You clicked OK (value = {messagebox})")
    else:
        my_label.config(text=f"You closed the window (value = {messagebox})")


# Create show_info function
# * Only shows OK button
def show_info():
    # ok
    messagebox = Messagebox.show_info("Please read.", "Voting time!")

    # Set Label to show which button was clicked
    my_label.config(text=f"messagebox = {messagebox}")


# Create show_error function
# * Shows OK button, plays error/alert sound
def show_error():
    # ok
    messagebox = Messagebox.show_error("Oops ...", "Voting time!")

    # Set Label to show which button was clicked
    my_label.config(text=f"messagebox = {messagebox}")


# Create show_question function
# * Shows YES and NO buttons, plays alert sound
def show_question():
    # ok
    messagebox = Messagebox.show_question("What say ye?", "Voting time!")

    # Set Label to show which button was clicked
    if messagebox == "No":  # When using Messagebox.show_question
        my_label.config(text=f"You clicked: {messagebox} ❌")
    elif messagebox == "Yes":
        my_label.config(text=f"You clicked: {messagebox} ✔")
    else:
        my_label.config(text=f"You closed the window {messagebox}")


# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Create Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

# Create Frame


# Create Button
my_button = tb.Button(root, text="yes/no", bootstyle="warning outline", command=yesno)
my_button.pack(side="left", padx=10)

my_button = tb.Button(root, text="ok", bootstyle="success", command=ok)
my_button.pack(side="left", padx=10)

my_button = tb.Button(
    root, text="ok/cancel", bootstyle="info outline", command=okcancel
)
my_button.pack(side="left", padx=10)

my_button = tb.Button(root, text="show info", bootstyle="info", command=show_info)
my_button.pack(side="left", padx=10)

my_button = tb.Button(
    root, text="show error    🔊", bootstyle="danger", command=show_error
)
my_button.pack(side="left", padx=10)

my_button = tb.Button(
    root, text="show question    🔊", bootstyle="warning outline", command=show_question
)
my_button.pack(side="left", padx=10)

root.mainloop()
