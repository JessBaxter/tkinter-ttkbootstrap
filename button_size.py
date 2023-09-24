from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
root.geometry("500x350")

# ! HACK to make font size bigger on button
# ? The "success." prefix sets the colour (i.e. green)
# Style
my_style = tb.Style()
# Style the font and button colour (green)
my_style.configure("success.TButton", font=("Helvetica", 18))
# ? The .Outline sets the type of button (must be capitalised) --> Outline, Link
# my_style.configure("success.Outline.TButton", font=("Helvetica", 18))

# Create a button
# ? width = number of characters, not the number of pixels
# my_button = tb.Button(text="Hello World!", width=30)
my_button = tb.Button(text="Hello World!", style="success.TButton")
my_button.pack(pady=40)


root.mainloop()
