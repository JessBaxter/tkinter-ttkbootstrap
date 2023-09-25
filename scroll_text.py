from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/

# ! REQUIRED for text box with scrollbar
from ttkbootstrap.scrolled import (
    ScrolledText,
)

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
# root.iconbitmap(default='images/codemy.ico')
root.geometry("700x350")

# Create ScrolledText widget
# ! REF: https://ttkbootstrap.readthedocs.io/en/latest/api/scrolled/scrolledtext/
my_text = ScrolledText(
    root,
    height=20,
    width=110,
    wrap=WORD,  # stops word from being split
    # autohide=True, # default False
    bootstyle="light round",
)
my_text.pack(pady=20)

root.mainloop()
