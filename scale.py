from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")

# Create a Scale/Slider
my_scale = tb.Scale(root, bootstyle="warning")
my_scale.pack(pady=50)

root.mainloop()
