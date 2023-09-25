# https://ttkbootstrap.readthedocs.io/en/latest/gallery/textreader/
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText

# ! Random selection from list
from random import choice


class TextReader(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=15)
        self.filename = tb.StringVar()
        self.pack(fill=BOTH, expand=YES)
        self.create_widget_elements()

    def create_widget_elements(self):
        """Create and add the widget elements"""
        style = tb.Style()
        self.textbox = ScrolledText(
            master=self,
            highlightcolor=style.colors.primary,
            highlightbackground=style.colors.border,
            highlightthickness=1,
        )
        self.textbox.pack(fill=BOTH)
        default_txt = "Click the browse button to open a new text file."
        self.textbox.insert(END, default_txt)

        browse_btn = tb.Button(self, text="Browse", command=self.open_file)
        browse_btn.pack(side=RIGHT, fill=X, padx=(5, 0), pady=10)

        # Add a Label to display a random line from the text file
        self.random_line_label = tb.Label(self, text="")
        self.random_line_label.pack(side=LEFT, fill=X, expand=YES, padx=(0, 5), pady=10)

        # Add a button to choose a new random line
        self.random_line_button = tb.Button(
            self,
            text="Choose Random Line",
            command=self.choose_random_line,
            state=DISABLED,  # Initial state is disabled until user loads a text file
        )
        self.random_line_button.pack(side=RIGHT, fill=X, padx=(5, 0), pady=10)

    def choose_random_line(self):
        if self.lines:
            random_line = choice(self.lines)
            self.random_line_label.config(
                text=f"{random_line.strip()}", font=("Helvetica", 18)
            )

    def open_file(self):
        path = askopenfilename()
        if not path:
            return

        with open(path, encoding="utf-8") as f:
            self.lines = f.readlines()
            if self.lines:
                self.choose_random_line()

            self.textbox.delete("1.0", END)
            self.textbox.insert(END, "".join(self.lines))
            self.filename.set(path)
            self.random_line_button.config(state=NORMAL)  # Enable random line button


if __name__ == "__main__":
    app = tb.Window("Text Reader", "sandstone")
    TextReader(app)
    app.mainloop()
