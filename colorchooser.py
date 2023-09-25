from tkinter import *  # https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import ttkbootstrap as tb  # https://ttkbootstrap.readthedocs.io/en/latest/
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

root = tb.Window(themename="superhero")
# LIGHT: https://ttkbootstrap.readthedocs.io/en/latest/themes/light/
# DARK: https://ttkbootstrap.readthedocs.io/en/latest/themes/dark/

# root = Tk()
root.title("TTK Bootstrap: Color Chooser")
# root.iconbitmap('images/codemy.ico')
root.geometry("700x350")


# Create chooser function
def chooser():
    # ! REQUIRES from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
    # Create color chooser
    my_color = ColorChooserDialog()
    # Show color chooser
    my_color.show()
    # Return color chooser info
    colors = my_color.result

    # Display the HEX colour
    hex_label.config(text=f"HEX: {colors.hex}")

    # Format (to remove parentheses) and display RGB
    rgb_values = colors.rgb
    rgb_values_formatted = f"{rgb_values[0]}, {rgb_values[1]}, {rgb_values[2]}"
    rgb_label.config(text=f"RGB: {rgb_values_formatted}")

    # Format (to remove parentheses) and display HSL
    hsl_values = colors.hsl
    hsl_values_formatted = f"{hsl_values[0]}, {hsl_values[1]}, {hsl_values[2]}"
    hsl_label.config(text=f"HSL: {hsl_values_formatted}")

    # Change swatch colour to user's selection
    my_style.configure("custom.TFrame", background=colors.hex, relief="solid")


def copyhex():
    # Retrieve the HEX color from the label
    hex_color = hex_label.cget("text").split(": ")[1]
    copy_to_clipboard(hex_color)


def copyrgb():
    # Retrieve the RGB color from the label and remove parentheses
    rgb_color = rgb_label.cget("text").split(": ")[1].replace("(", "").replace(")", "")
    copy_to_clipboard(rgb_color)


def copyhsl():
    # Retrieve the HSL color from the label and remove parentheses
    hsl_color = hsl_label.cget("text").split(": ")[1].replace("(", "").replace(")", "")
    copy_to_clipboard(hsl_color)


def copy_to_clipboard(value):
    clipboard_root = Tk()
    clipboard_root.withdraw()
    clipboard_root.clipboard_clear()
    clipboard_root.clipboard_append(value)
    clipboard_root.update()
    clipboard_root.destroy()


# Colours: primary, secondary, success, info, warning, danger, light, dark
# STYLE GUIDE: https://ttkbootstrap.readthedocs.io/en/latest/styleguide/

# Define subclass for existing style
my_style = tb.Style()
my_style.configure("custom.TFrame", background="white", relief="solid")

# Create main Frame
my_frame = Frame(root)
my_frame.pack()

# Create app Label
app_label = tb.Label(
    my_frame, bootstyle="warning", text="Colour Picker", font=("Arial Black", 30)
)
app_label.grid(column=0, row=0, columnspan=4, pady=40)

# Create color swatch Frame
color_swatch = tb.Frame(my_frame, width=100, height=100, style="custom.TFrame")
color_swatch.grid(column=0, row=1, pady=10, rowspan=3)

# Create picker Button
my_button = tb.Button(
    my_frame, text="Picker", bootstyle="warning", width=12, command=chooser
)
my_button.grid(column=0, row=4, padx=40)


# Create HEX heading Label
hex_heading = tb.Label(
    my_frame, text="HEX:", bootstyle="light", font=("Arial Black", 12)
)
hex_heading.grid(column=1, row=1, padx=10, sticky="e")

# Create HEX value Label
hex_label = tb.Label(my_frame, text="#ffffff", font=("Helvetica", 14))
hex_label.grid(column=2, row=1, sticky="w")

# Create HEX copy button
copyhex_button = tb.Button(my_frame, text="copy", bootstyle="light", command=copyhex)
copyhex_button.grid(column=3, row=1, padx=10, sticky="w")


# Create RGB heading Label
hex_heading = tb.Label(
    my_frame, text="RGB:", bootstyle="light", font=("Arial Black", 12)
)
hex_heading.grid(column=1, row=2, padx=10, sticky="e")

# Create RGB values Label
rgb_label = tb.Label(my_frame, text="255, 255, 255", font=("Helvetica", 14))
rgb_label.grid(column=2, row=2, sticky="w")

# Create RGB copy button
copyrgb_button = tb.Button(my_frame, text="copy", bootstyle="light", command=copyrgb)
copyrgb_button.grid(column=3, row=2, padx=10, sticky="w")


# Create HSL heading Label
hex_heading = tb.Label(
    my_frame, text="HSL:", bootstyle="light", font=("Arial Black", 12)
)
hex_heading.grid(column=1, row=3, padx=10, sticky="e")

# Create HSL values Label
hsl_label = tb.Label(my_frame, text="0, 0, 100", font=("Helvetica", 14))
hsl_label.grid(column=2, row=3, sticky="w")

# Create HSL copy button
copyhsl_button = tb.Button(my_frame, text="copy", bootstyle="light", command=copyhsl)
copyhsl_button.grid(column=3, row=3, padx=10, sticky="w")


root.mainloop()
