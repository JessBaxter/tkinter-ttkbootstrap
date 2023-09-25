from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/


root = tb.Window(themename="superhero")


# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
# root.iconbitmap(default='images/codemy.ico')
root.geometry("500x350")

# Create Frame
# ! EASIER TO USE ScrolledFrame here 👉 scroll_frame.py
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create Scrollbar
my_scroll = tb.Scrollbar(
    # REF: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/scrollbar/
    my_frame,
    orient="vertical",
    bootstyle="dark round",  # rounded bar
)
my_scroll.pack(side="right", fill="y")  # fill="y" -> y-axis

# Create Text
# ! EASIER TO USE ScrolledText here 👉 scroll_text.py
my_text = Text(
    my_frame,
    width=30,
    height=25,
    yscrollcommand=my_scroll.set,  # Tkinter
    wrap="none",
    font=("Helvetica", 18),
)
my_text.pack()

# Config Scrollbar
my_scroll.config(command=my_text.yview)  # Moving the scrollbar moves my_text


root.mainloop()
