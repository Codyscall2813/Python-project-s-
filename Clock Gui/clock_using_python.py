import tkinter as tk
import time
from tkinter import font as tkfont

def update_time():
    # Get the current time in 12-hour format with AM/PM
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("800x200")
root.configure(bg='purple')

custom_font = tkfont.Font(family="DS-Digital", size=120, weight="bold")

# Create a label to display the time
time_label = tk.Label(root, font=custom_font, background='#0C359E', foreground='white')
time_label.pack(expand=True, fill='both')

update_time()
# Run the main application loop
root.mainloop()
