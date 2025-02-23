# I was printing all output to the terminal for debugging purposes.

import tkinter as tk
import math
from tkinter import PhotoImage

# Button Functions
def button_click(text):
    current_text = display.get()
    print(f"Current Text: {current_text}")
    print(f"Button Clicked: {text}")

    if text == "C":
        display.delete(0, tk.END)
    elif text == "⌫":
        display.delete(len(current_text) - 1)
    elif text == "CE":
        display.delete(0, tk.END)
    elif text == "=":
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            print(f"Result: {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    elif text == "√x":
        try:
            result = math.sqrt(float(current_text))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            print(f"Square Root: {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    elif text == "x^2":
        try:
            result = float(current_text) ** 2
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            print(f"Square: {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    elif text == "1/x":
        try:
            result = 1 / float(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            print(f"Reciprocal: {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    elif text == "%":
        try:
            result = float(current_text) / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
            print(f"Percentage: {result}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    elif text == "+/-":
        try:
            if current_text.startswith('-'):
                display.delete(0)
            else:
                display.insert(0, '-')
            print(f"Toggle Sign: {display.get()}")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            print(f"Error: {e}")
    else:
        display.insert(tk.END, text)

# Fuction for button creation
def create_button(text, row, col, rowspan=1, colspan=1):
    bg_color = "#1372F3" if text == "=" else None
    fg_color = "white" if text == "=" else None
    button = tk.Button(root, text=text, padx=10, pady=5, font=(
        "Fira Code SemiBold", 14), command=lambda: button_click(text), bg=bg_color, fg=fg_color)
    button.grid(row=row, column=col, rowspan=rowspan,
                columnspan=colspan, padx=1, pady=1, sticky='nsew')


# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("280x320")
root.resizable(False, False)
icon_path = "Collection/Calculator Gui/icon.png"
icon_image = PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)

# Display
display = tk.Entry(root, font=("Fira Code SemiBold", 20), bd=10,
                   insertwidth=2, width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Create buttons
buttons = [
    ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
    ('1/x', 2, 0), ('x^2', 2, 1), ('√x', 2, 2), ('+', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('/', 5, 3),
    ('+/-', 6, 0), ('0', 6, 1), ('.', 6, 2), ('=', 6, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    create_button(text, row, col)

# Start the loop
root.mainloop()
