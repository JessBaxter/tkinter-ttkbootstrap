from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = TK()
root.title = "TTK Bootstrap"
# root.iconbitmap("images/codemy.ico")
root.geometry("500x350")


def checker():
    if var1.get() == 1:
        my_label.config(text="Checked")
    else:
        my_label.config(text="Unchecked")


# Label
# ! FIX for "SyntaxError: positional argument follows keyword argument"
# ! font requires value(s) to be enclosed in parentheses
# * --> font=("Helvetica", 18)
my_label = Label(text="Check the 'Checkbutton' below", font=("Helvetica", 18))
# Padding: 40 on top and 10 below
my_label.pack(pady=(40, 10))

# Checkbutton
# ? IntVar is a tkinter int variable. checked = 1, unchecked = 0
var1 = IntVar()
my_check = tb.Checkbutton(
    bootstyle="primary",
    text="Check me",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check.pack(side=RIGHT, padx=5, pady=10)

var1a = IntVar()
my_check1a = tb.Checkbutton(
    bootstyle="primary",
    text="or check me",
    variable=var1a,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check1a.pack(side=RIGHT, padx=5, pady=10)

# my_separator = tb.Separator()
my_separator = tb.Separator(bootstyle="info")
my_separator.pack()

# ToolButton
var2 = IntVar()
my_check2 = tb.Checkbutton(
    bootstyle="danger, toolbutton",
    text="ToolButton",
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check2.pack(side=LEFT, padx=5, pady=10)

var2a = IntVar()
my_check2a = tb.Checkbutton(
    bootstyle="danger, toolbutton",
    text="ToolButton 2a",
    variable=var2a,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check2a.pack(side=LEFT, padx=5, pady=10)

# Outlined ToolButton
var3 = IntVar()
my_check3 = tb.Checkbutton(
    bootstyle="success, toolbutton, outline",
    text="Outlined ToolButton",
    variable=var3,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check3.pack(pady=10)

# Round Toggle Button
var4 = IntVar()
my_check4 = tb.Checkbutton(
    bootstyle="success, round-toggle",
    text="Round Toggle Button",
    variable=var4,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check4.pack(pady=10)

# Square Toggle Button
var5 = IntVar()
my_check5 = tb.Checkbutton(
    bootstyle="success, square-toggle",
    text="Square Toggle Button",
    variable=var5,
    onvalue=1,
    offvalue=0,
    command=checker,
)
my_check5.pack(pady=10)

root.mainloop()
