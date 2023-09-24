from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Menu Button")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")

#
#
#
# You can style the menu items with the tkinter Style widget (see button_size.py)
#
#
#
#


# Create a function to display which item was selected by user
def stuff(x):
    # my_label.config(text=x)
    my_label.config(text=f"You selected: {x}")
    my_menu.config(bootstyle=x)  # Menubutton changes to selected style


# Create Menubutton
my_menu = tb.Menubutton(root, bootstyle="warning", text="Please choose...")
my_menu.pack(pady=50)

# Create menu items
menu_content = tb.Menu(my_menu)

# Add items to menu
menu_item = StringVar()
for x in [
    "primary",
    "secondary",
    "danger",
    "info",
    "outline primary",
    "outline secondary",
    "outline danger",
    "outline info",
]:  # ! REMEMBER colon here because loop
    menu_content.add_radiobutton(
        # * need lambda here
        label=x,  # label is all lowercase
        variable=menu_item,
        command=lambda x=x: stuff(x),  # x=x stops loop from only show last item in list
    )

# Associate menu_content with the Menubutton
my_menu["menu"] = menu_content

# Create a label
my_label = tb.Label(root, text="")
my_label.pack(pady=40)

root.mainloop()
