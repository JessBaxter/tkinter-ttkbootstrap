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

# Create XXX function

# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Create Label
label1 = tb.Label(root, text="Some text here", bootstyle="light")
label1.pack(pady=40)

# Separator
my_separator = tb.Separator(
    root,
    bootstyle="warning",
    # orient="vertical", # default horizontal
)
my_separator.pack(
    fill="x",  # Increase size to fill width of window
    padx=20,  # Add padding to pull line in from edges of window
)

label2 = tb.Label(root, text="Some other text here", bootstyle="light")
label2.pack(pady=40)

root.mainloop()
