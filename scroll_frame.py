from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/
from ttkbootstrap.scrolled import ScrolledFrame

root = tb.Window(themename="superhero")


# root = Tk()
root.title("TTK Bootstrap Scrolled Frame")
# root.iconbitmap('images/codemy.ico')
# root.iconbitmap(default='images/codemy.ico')
root.geometry("700x350")

# Create app Label
app_label = tb.Label(
    root,
    bootstyle="light",
    text="Frame with built-in scrollbar",
    font=("Arial Black", 20),
)
app_label.pack(pady=20)

# Create ScrolledFrame widget
my_frame = ScrolledFrame(root, bootstyle="dark rounded")
my_frame.pack(
    pady=20,
    padx=20,
    fill=BOTH,  # Make frame fit screen
    expand=YES,  # Make frame fit screen
)

# Create placeholder Buttons
for x in range(21):
    tb.Button(my_frame, bootstyle="light", text=f"Click me {x}").pack(pady=20)


root.mainloop()
