from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/

# ! REQUIRED for toasts
from ttkbootstrap.toast import ToastNotification

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap")
# root.iconbitmap('images/codemy.ico')
# root.iconbitmap(default='images/codemy.ico')
root.geometry("300x200")


def clicker():
    toast.show_toast()


# Create ToastNotification
toast = ToastNotification(
    title="Toast Title",
    message="This is the toast message",
    duration=3000,  # Perma(?) without duration (CLICK TOAST TO CLOSE IT)
    alert=True,  # Adds alert sound
    # position=(-1920, 30, 'sw'), # Moves it from the default, main monitor position
    #   * DEFAULT position is bottom right, above taskbar
)

button = tb.Button(root, text="Toast me", command=clicker)
button.pack(pady=40)

root.mainloop()
