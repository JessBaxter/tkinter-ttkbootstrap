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

# Create Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create Scrollbar
my_scroll = tb.Scrollbar(
    # REF: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/scrollbar/
    my_frame,
    orient="vertical",
    bootstyle="dark round",  # rounded bar
)
my_scroll.pack(side="right", fill="y")  # fill="y" -> y-axis

# Create Text
my_text = Text(
    my_frame,
    width=30,
    height=25,
    yscrollcommand=my_scroll.set,  # Tkinter
    wrap="none",
    font=("Helvetica", 18),
)
my_text.pack()

# Config Scrollbar
my_scroll.config(command=my_text.yview)  # Moving the scrollbar moves my_text


root.mainloop()
