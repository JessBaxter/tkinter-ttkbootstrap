from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")


def thing():
    pass


# Create a bootstrap-styled Frame
# my_frame = tb.Frame(root, bootstyle="dark")
# my_frame.pack(pady=40)

# Create an invisible frame so we can use grid inside it
my_frame = Frame(root)
my_frame.pack(pady=40)


# Create a text box
my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

# Create a button
my_button = tb.Button(my_frame, text="Click me!", bootstyle="light", command=thing)
my_button.pack(pady=20, padx=20)

# Create a Label
my_label = tb.Label(
    root, text="I am not a button", font=("Helvetica", 18), bootstyle="inverse light"
)
my_label.pack(pady=20)

root.mainloop()
