from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")


# Define the scaler function
# * Pass in e(vent), so user moving slider pushes an event into this function
def scaler(e):
    # Wrap the my_scale.get() function in a Python integer function
    # * This converts floating point into whole numbers
    my_label.config(text=f"{int(my_scale.get())}%")
    # FLOATING POINT --> my_label.config(text=f"{my_scale.get()}")


# Create a Scale/Slider
my_scale = tb.Scale(
    root,
    bootstyle="warning",
    length=400,  # Physical length, not max value
    # orient="vertical",  # default horizontal
    from_=0,  # from_ attribute is used because from is a Python keyword
    to=100,  # max value
    command=scaler,
    # state="disable",  # default 'normal'
)
my_scale.pack(pady=50)

# Create Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack()

root.mainloop()
