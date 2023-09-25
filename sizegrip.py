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

# Create Label
my_label = tb.Label(root, text="Here is some text", font=("Helvetica", 18))
my_label.pack(pady=20)

# Create Sizegrip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(
    anchor="se",  # Move from middle of window to South-East (aligned to window content)
    # fill="both",  # ? What does this do?
    # expand="true",  # Move to SE of app window
)

root.mainloop()
