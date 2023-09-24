from tkinter import *
import ttkbootstrap as tb

# time python library required for auto function
import time

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Progress Bar")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x250")


# Define start function
def start():
    my_progress.start(10)


# Define stop function
def stop():
    my_progress.stop()
    my_label.config(text=my_progress["value"])


def auto():
    for x in range(5):  # 20 x 5 = 100 (max timer length)
        my_progress["value"] += 20
        my_label.config(text=my_progress["value"])
        # ! FIX for bar not updating until loop is completed
        root.update_idletasks()
        # Increment every 1 second
        time.sleep(1)


# Define Increment function
def increment():
    if my_progress["value"] < 100:
        # * Pass in the value attribute
        # * (instead of .step, so that it fills the bar to 100% instead of 80%)
        my_progress["value"] += 20
        # Get current value
        my_label.config(text=my_progress["value"])
    else:
        pass


# Create Progressbar
my_progress = tb.Progressbar(
    root,
    bootstyle="danger striped",
    maximum=100,  # default = 100
    mode="determinate",  # default = determinate
    length=300,  # NOT the same as maximum
    value=0,
)
my_progress.pack(pady=20)

# Create Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create Button
my_button = tb.Button(my_frame, text="Inc 20", bootstyle="info", command=increment)
my_button.grid(column=0, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="Start", bootstyle="info", command=start)
my_button2.grid(column=1, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="Stop", bootstyle="info", command=stop)
my_button3.grid(column=2, row=0, padx=10)

my_button4 = tb.Button(my_frame, text="Auto", bootstyle="info", command=auto)
my_button4.grid(column=3, row=0, padx=10)


# Create Label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()
