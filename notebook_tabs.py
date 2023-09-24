from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = Tk()
root.title("TTK Bootstrap: Notebook Tabs")
# root.iconbitmap('images/codemy.ico')
root.geometry("1000x450")

# Create Notebook
my_notebook = tb.Notebook(root, bootstyle="dark")
# my_notebook.pack(pady=20)
my_notebook.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

# * Create Frames to function as the tabs
# Create Frames
tab1 = tb.Frame(my_notebook)
tab2 = tb.Frame(my_notebook)

# * Put stuff in the first tab/frame
# Create (tkinter) Label
my_label = Label(tab1, text="My First tab", font=("Helvetica", 18))
my_label.pack(pady=20)

# Create (tkinter) Text
my_text = Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

# Create Button
my_button = tb.Button(tab1, text="Click me", bootstyle="danger outline")
my_button.pack(pady=20)

# * Put stuff in the second tab/frame
# Create (tkinter) Label
my_label2 = Label(tab2, text="My Second tab", font=("Helvetica", 18))
my_label2.pack(pady=20)

# Create (tkinter) Text
my_text2 = Text(tab2, width=70, height=10)
my_text2.pack(pady=10, padx=10)

# Create Button
my_button2 = tb.Button(tab2, text="Click me", bootstyle="success outline")
my_button2.pack(pady=20)


# Add frames to the Notebook
my_notebook.add(tab1, text="Tab One")
my_notebook.add(tab2, text="Tab Two")


# Create second Notebook
my_notebook2 = tb.Notebook(root, bootstyle="dark")
# my_notebook2.pack(pady=20)
my_notebook2.grid(row=0, column=1, padx=20, pady=20, sticky="ns")


# * Create Frames to function as the tabs
# Create Frames
tab3 = tb.Frame(my_notebook2)
tab4 = tb.Frame(my_notebook2)

# * Put stuff in the third tab/frame
# Create (tkinter) Label
my_label3 = Label(tab3, text="My Third tab", font=("Helvetica", 18))
my_label3.pack(pady=20)

# Create (tkinter) Text
my_text3 = Text(tab3, width=70, height=10)
my_text3.pack(pady=10, padx=10)

# * Put stuff in the fourth tab/frame
# Create (tkinter) Label
my_label4 = Label(tab4, text="My Fourth tab", font=("Helvetica", 18))
my_label4.pack(pady=20)

# Create (tkinter) Text
my_text4 = Text(tab4, width=70, height=10)
my_text4.pack(pady=10, padx=10)

# Add frames to the second Notebook
my_notebook2.add(tab3, text="Tab Three")
my_notebook2.add(tab4, text="Tab Four")

# Configure rows to make notebooks the same size
root.grid_rowconfigure(0, weight=1)

root.mainloop()
