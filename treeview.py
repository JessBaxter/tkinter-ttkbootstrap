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
root.geometry("700x350")

# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Create Frame for Scrollbar to attach to
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create Scrollbar
my_scroll = tb.Scrollbar(
    my_frame,
    orient="vertical",
    bootstyle="dark round",
)
my_scroll.pack(side="right", fill="y")

# Define Columns
columns = ("first_name", "last_name", "email")  # Immutable Tuple

# Create Treeview
my_tree = tb.Treeview(
    my_frame,
    bootstyle="dark",
    columns=columns,  # Use the "columns" mutable list above
    show="headings",  # Show headings at top of each column, as defined below
    yscrollcommand=my_scroll.set,
)
my_tree.pack()  # No padding because inside Frame with Scrollbar

# Define headings
my_tree.heading("first_name", text="First Name")
my_tree.heading("last_name", text="Last Name")
my_tree.heading("email", text="Email Address")

# Create Sample Data
contacts = []  # Empty mutable list

# * Fill empty list (NOT array) with fake info
for n in range(1, 20):
    # Auto generate Bob 1, Bobby 1, email1@bob.com ... Bob 20, Bobby 20, bob20@bob.com
    contacts.append((f"Bob {n}", f"Bobby {n}", f"bob{n}@bob.com"))

# Add Data to Treeview
for contact in contacts:
    my_tree.insert(
        "",  # from (0)
        END,  # to
        values=contact,  # Items in contacts list
    )


# Config Scrollbar
my_scroll.config(command=my_tree.yview)

root.mainloop()
