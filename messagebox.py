# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/api/validation/
# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/cookbook/validate-user-input/
# API: https://ttkbootstrap.readthedocs.io/en/latest/api/

# [...] = A list - mutable
# (...) = A tuple - immutable

from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/
from ttkbootstrap.dialogs import Messagebox  # Required for Messagebox

# from datetime import date  # Allows you to set startdate in tb.DateEntry()
# from ttkbootstrap.dialogs import Querybox  # Allows Button to bring up calendar

root = tb.Window(themename="superhero")
# LIGHT: https://ttkbootstrap.readthedocs.io/en/latest/themes/light/
# DARK: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/

# root = Tk()
root.title("TTK Bootstrap: Message Box")
# Main app icon
# root.iconbitmap('images/codemy.ico')
# Messagebox Icon
# root.iconbitmap(default='images/codemy.ico')
root.geometry("700x350")


# Create clicker function
def clicker():
    # Create a dialog
    # yesno
    Messagebox.yesno("Some message here", "This is the title")


# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Create Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

# Create Frame


# Create Button
my_button = tb.Button(root, text="Click me", bootstyle="info", command=clicker)
my_button.pack(pady=40)

root.mainloop()
