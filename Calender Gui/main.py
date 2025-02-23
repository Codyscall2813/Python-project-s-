import calendar
import tkinter as tk
from tkinter import ttk, PhotoImage
from datetime import datetime

# Function to convert month name to month number
def month_name_to_number(month_name):
    month_number = list(calendar.month_name).index(month_name)
    return month_number

# Function to update the calendar display
def show_calendar():
    try:
        month_name = month_combobox.get()
        year = int(year_entry.get())
        month_number = month_name_to_number(month_name)
        cal_text = calendar.month(year, month_number)
        cal_textbox.delete(1.0, tk.END)
        cal_textbox.insert(tk.END, cal_text)
    except ValueError:
        cal_textbox.delete(1.0, tk.END)
        cal_textbox.insert(tk.END, "Invalid input. Please enter a valid year.")

# Create the main window
root = tk.Tk()
root.title("Calendar Viewer")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='Collection/Calender Gui/calendar.png'))
root.resizable(False, False)

# Get the current month and year
now = datetime.now()
current_month_name = calendar.month_name[now.month]
current_year = now.year

# Create and place widgets using grid layout
input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

# Container for month selection
month_frame = tk.Frame(input_frame)
month_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Month Label and Combobox
month_label = tk.Label(month_frame, text="Select Month:")
month_label.grid(row=0, column=0, sticky=tk.W)
month_combobox = ttk.Combobox(month_frame, values=list(calendar.month_name[1:]))
month_combobox.set(current_month_name)  # Set default month
month_combobox.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

# Container for year entry
year_frame = tk.Frame(input_frame)
year_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Year Label and Entry
year_label = tk.Label(year_frame, text="Enter Year:")
year_label.grid(row=0, column=0, sticky=tk.W)
year_entry = tk.Entry(year_frame)
year_entry.insert(0, str(current_year))  # Set default year
year_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W+tk.E)

# Show button
show_button = tk.Button(input_frame, text="Show Calendar", command=show_calendar)
show_button.grid(row=1, column=0, columnspan=2, pady=10, padx=(11, 0), sticky=tk.W)

# Make the calendar output larger
cal_textbox = tk.Text(root, height=7, width=20, font=("Courier", 18))
cal_textbox.pack(pady=10, padx=10)

# Show the calendar for the current month and year by default
show_calendar()

# Start the Tkinter event loop
root.mainloop()