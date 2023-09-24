from tkinter import *
import ttkbootstrap as tb

from datetime import date  # Allows you to set startdate in tb.DateEntry()
from ttkbootstrap.dialogs import Querybox  # Allows button to bring up calendar

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")


# Create Function to get the selected date
def datey():
    # Grab the date
    my_label.config(text=f"You picked: {my_date.entry.get()}")


# Create Function to show the calendar
def calendar():
    # ? REF: https://ttkbootstrap.readthedocs.io/en/latest/api/dialogs/querybox/
    cal = Querybox()  # Querybox requires ttkbootstrap.dialogs library
    my_label.config(text=f"You picked: {cal.get_date()}")


# Create DateEntry widget
# ? startdate requires datetime library
# ? firstweekday requires datetime library
# ? (0 = M, 1 = Tu, 2 = W, 3 = Th, 4 = F, 5 = Sa, 6 = Su)
my_date = tb.DateEntry(
    root, bootstyle="danger", firstweekday=0, startdate=date(2023, 4, 1)
)
my_date.pack(pady=(50, 10))

# Create Button
my_button = tb.Button(root, text="Get date", bootstyle="danger outline", command=datey)
my_button.pack(pady=(20, 50))

# Create Calendar Button
my_button2 = tb.Button(
    root, text="Show calendar", bootstyle="success", command=calendar
)
my_button2.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
