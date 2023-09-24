from tkinter import *

# ! FIX for AttributeError: module 'PIL.Image' has no attribute 'CUBIC'. Did you mean: 'BICUBIC'?
from PIL import Image

# ! also this second line (auto-formatter stuffing things up)
Image.CUBIC = Image.BICUBIC

import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Meter Widget")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x550")


# Create Function to handle step up button
# ! ISSUE: Keep clicking and counter goes down then up again
def up():
    my_meter.step(10)


# Create Function to handle step down button
# ! ISSUE: Keep clicking and counter goes negative
def down():
    my_meter.step(-10)


# Create global variable
global counter
counter = 20


# Create Function to handle clicking button
def clicker():
    global counter
    if counter <= 100:  # ! FIX for counter going above 100/max value
        my_meter.configure(amountused=counter)
        counter += 20
        my_button.configure(text=f"Click me {my_meter.amountusedvar.get()}")


# Create Meter
# ? REF: https://ttkbootstrap.readthedocs.io/en/latest/api/widgets/meter/#ttkbootstrap.widgets.Meter.__init__
my_meter = tb.Meter(
    root,  # Attach to this component (i.e. the main window)
    bootstyle="warning",  # Colour
    subtext="Tkinter Learnt",  # Text inside circle
    subtextstyle="warning",  # Text colour
    interactive=True,  # Allow user to click and drag meter amount/value
    textright="%",  # Add text to the right of the value
    # textleft="$",
    # metertype="semi",  # default = full (semi looks like a speedometer)
    stripethickness=10,  # Adds dashes/segments to meter
    # metersize=400,  # Scale's the size of the meter
    # padding=50,  # Outside padding
    # amountused=20,  # Starts at this value
    # amounttotal=150,  # Max value
)
my_meter.pack(pady=50)

# Create Button
my_button = tb.Button(root, text="Click me", command=clicker)
my_button.pack(pady=20)

my_button2 = tb.Button(root, bootstyle="warning", text="Step up", command=up)
my_button2.pack(pady=20)

my_button3 = tb.Button(root, bootstyle="info", text="Step down", command=down)
my_button3.pack(pady=20)

root.mainloop()
