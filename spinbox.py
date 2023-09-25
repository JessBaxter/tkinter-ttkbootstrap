# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/api/validation/
# VALIDATION: https://ttkbootstrap.readthedocs.io/en/latest/cookbook/validate-user-input/
# API: https://ttkbootstrap.readthedocs.io/en/latest/api/


from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/

# from datetime import date  # Allows you to set startdate in tb.DateEntry()
# from ttkbootstrap.dialogs import Querybox  # Allows Button to bring up calendar

root = tb.Window(themename="superhero")
# LIGHT: https://ttkbootstrap.readthedocs.io/en/latest/themes/light/
# DARK: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")


# Create spinny function
def spinny():
    my_label.config(text=my_spin.get())


# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Spinbox list
stuff = ["John", "Barry", "Harry", "Larry"]

# Create Spinbox
my_spin = tb.Spinbox(
    root,
    bootstyle="success",
    font=("Helvetica", 18),
    # from_=0,  # Using from_ because from is Python keyword
    # to=10,
    values=stuff,  # Use stuff array instead of # 1-10
    state="readonly",  # Removes text highlight and disables editing
    # command=spinny, # Auto change Label when cycling through Spinbox items
)
my_spin.pack(pady=20)

# Set Spinbox default
my_spin.set("John")  # Replaces the empty Spinbox with this on first load

# Create Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

# Create Frame

# Create Button
my_button = tb.Button(root, text="Click me", bootstyle="success", command=spinny)
my_button.pack(pady=20)

root.mainloop()
