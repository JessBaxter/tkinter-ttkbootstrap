# https://stackoverflow.com/a/38678891
import tkinter as tk
import ttkbootstrap as tb
import time


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")

        # Remove the title bar
        self.overrideredirect(True)

        # Add a label with the loading text
        label = tb.Label(
            self, text="Loading...", bootstyle="dark", font=("Arial Black", 30)
        )
        label.pack(padx=20, pady=20)

        # Calculate the position to center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 600  # Width of the splash window
        height = 300  # Height of the splash window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        ## required to make window show before the program gets to the mainloop
        self.update()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        ## simulate a delay while loading
        time.sleep(6)

        ## finished loading so destroy splash
        splash.destroy()

        # Calculate the position to center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 1000  # Width of the splash window
        height = 800  # Height of the splash window
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")

        ## show window again
        self.deiconify()


if __name__ == "__main__":
    app = App()
    app.mainloop()
