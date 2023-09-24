from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Floodgauge")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x550")


# Create a Function to start the floodgauge
def starter():
    # ? speed of gauge is more erratic when adding a value
    my_gauge.start()  # (1) is FASTER, (5) is SLOWER


# Create a Function to stop the floodgauge
def stopper():
    my_gauge.stop()


# Create a Function to increment the floodgauge
def incrementer():
    my_gauge.step(10)  # click button = increment by 10(%)
    my_label.config(text=f"Position: {my_gauge.variable.get()}%")  # Show gauge %
    # * Do maths magic on my_gauge.variable, so 10 on gauge becomes 20 in label
    # my_label.config(
    #     text=f"Position: {my_gauge.variable.get() +10}" # 10 on gauge = 20 in label
    # )


# Create Floodgauge
my_gauge = tb.Floodgauge(
    root,
    bootstyle="success",
    font=("Helvetica", 18),
    mask="Pos: {}%",
    maximum=100,  # max length
    # orient="horizontal",  # default = horizontal
    # value=0,  # optionally start at another number/value
    # mode="indeterminate" # changes to square bouncing back & forth between min & max
)
my_gauge.pack(
    # fill=X --> must be capitalised
    pady=30,
    fill=X,  # width set to window width
    padx=20,  # adds padding left and right (since we've set to window width)
)

# Create a button to start the Floodgauge
start_button = tb.Button(
    root, text="Start", bootstyle="success outline", command=starter
)
start_button.pack(pady=20)

# Create a button to stop the Floodgauge
stop_button = tb.Button(root, text="Stop", bootstyle="warning outline", command=stopper)
stop_button.pack(pady=20)

# Create a button to increment the Floodgauge
inc_button = tb.Button(
    root, text="Increment", bootstyle="info outline", command=incrementer
)
inc_button.pack(pady=20)

# Create a Label
my_label = tb.Label(root, text="Position: ")
my_label.pack(pady=20)

root.mainloop()
