# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/api/validation/
# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/cookbook/validate-user-input/
# API: https://ttkbootstrap.readthedocs.io/en/latest/api/

# [...] = A list - mutable
# (...) = A tuple - immutable

from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/
from ttkbootstrap.dialogs import Messagebox  # ! Required for Messagebox
from constants import LARGER_BUTTON_WIDTH, BUTTON_WIDTH

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
        my_label.config(text=f"You closed the window (messagebox = {messagebox})")


# Create yesnocancel function
# * Shows YES and NO buttons
def yesnocancel():
    # Create a dialog
    # yesnocancel
    # ! NEED IMPORT: from ttkbootstrap.dialogs import Messagebox
    messagebox = Messagebox.yesnocancel("Yay, nay or gtfo?", "Voting time!")

    # Set Label to show which button was clicked
    if messagebox == "No":  # When using Messagebox.yesnocancel
        my_label.config(text=f"You clicked: {messagebox} ❌")
    elif messagebox == "Yes":
        my_label.config(text=f"You clicked: {messagebox} ✔")
    elif messagebox == "Cancel":
        my_label.config(text=f"You clicked: {messagebox}")
    else:
        my_label.config(text=f"You closed the window (messagebox = {messagebox})")


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


# Create retrycancel function
# * Shows RETRY and CANCEL buttons
def retrycancel():
    # ok
    messagebox = Messagebox.retrycancel("Redo or gtfo?", "Voting time!")

    # Set Label to show which button was clicked
    if messagebox == "Cancel":  # When using Messagebox.retrycancel
        my_label.config(text=f"You clicked CANCEL (value = {messagebox})")
    elif messagebox == "Retry":
        my_label.config(text=f"You clicked RETRY (value = {messagebox})")
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
        my_label.config(text=f"You closed the window (messagebox = {messagebox})")


# Create show_warning function
# * Shows OK button, plays error/alert sound
def show_warning():
    # ok
    messagebox = Messagebox.show_warning("Um ...", "Voting time!")

    # Set Label to show which button was clicked
    my_label.config(text=f"messagebox = {messagebox}")


# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Create Frame
my_frame = tb.Frame(
    root,
    borderwidth=2,  # This AND relief are required
    relief="solid",  # flat, raised, sunken, solid, ridge, groove
)
my_frame.pack(pady=20)

# Configure grid
my_frame.columnconfigure(0, weight=1)
my_frame.columnconfigure(1, weight=1)
my_frame.columnconfigure(2, weight=1)

# Create Label
my_label = tb.Label(
    my_frame,
    text="",
    font=("Helvetica", 18),
    width=50,  # Fixed width so it doesn't make the buttons move
    # wraplength=400,  # Wrap within fixed-width space
    anchor="center",  # Anchor position
)
my_label.grid(
    column=0,
    row=0,
    pady=20,
    columnspan=4,
    sticky="nsew",  # Expansion directions (nsew = entire cell)
)


# Create Buttons
# COLUMN 1 ===========================
# * PLEASE 👉 sticky="e"
ok_button = tb.Button(
    my_frame, text="ok", bootstyle="success", command=ok, width=BUTTON_WIDTH
)
ok_button.grid(column=0, row=1, padx=10, pady=10, sticky="e")


okcancel_button = tb.Button(
    my_frame,
    text="ok/cancel",
    bootstyle="success outline",
    command=okcancel,
    width=BUTTON_WIDTH,
)
okcancel_button.grid(column=0, row=2, padx=10, pady=10, sticky="e")


retrycancel_button = tb.Button(
    my_frame,
    text="retry/cancel",
    bootstyle="info outline",
    command=retrycancel,
    width=BUTTON_WIDTH,
)
retrycancel_button.grid(column=0, row=3, padx=10, pady=10, sticky="e")

# COLUMN 2 ===========================
yesno_button = tb.Button(
    my_frame,
    text="yes/no",
    bootstyle="light outline",
    command=yesno,
    width=BUTTON_WIDTH,
)
yesno_button.grid(column=1, row=1, padx=10, pady=10)

yesnocancel_button = tb.Button(
    my_frame,
    text="yes/no/cancel",
    bootstyle="light outline",
    command=yesnocancel,
    width=BUTTON_WIDTH,
)
yesnocancel_button.grid(column=1, row=2, padx=10, pady=10)


# COLUMN 3 ===========================
# * PLEASE 👉 sticky="w"
show_error_button = tb.Button(
    my_frame,
    text="show error    🔊",
    bootstyle="danger",
    command=show_error,
    width=LARGER_BUTTON_WIDTH,
)
show_error_button.grid(column=2, row=1, padx=10, pady=10, sticky="w")


show_question_button = tb.Button(
    my_frame,
    text="show question    🔊",
    bootstyle="light outline",
    command=show_question,
    width=LARGER_BUTTON_WIDTH,
)
show_question_button.grid(column=2, row=2, padx=10, pady=10, sticky="w")


show_warning_button = tb.Button(
    my_frame,
    text="show warning    🔊",
    bootstyle="warning",
    command=show_warning,
    width=LARGER_BUTTON_WIDTH,
)
show_warning_button.grid(column=2, row=3, padx=10, pady=10, sticky="w")


show_info_button = tb.Button(
    my_frame,
    text="show info",
    bootstyle="info",
    command=show_info,
    width=LARGER_BUTTON_WIDTH,
)
show_info_button.grid(column=2, row=4, padx=10, pady=10, sticky="w")


root.mainloop()
